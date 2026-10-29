#!/bin/zsh
# Makes the voiceover clips for "Solve it in your head" episodes from voice/cues.txt.
# Usage: ./mental-maths-voice.sh 10            (makes missing clips only)
#        ./mental-maths-voice.sh 10 --redo a2  (remakes one clip, e.g. a new take)
#        ./mental-maths-voice.sh 10 --redo all
# cues.txt lines are "start clip text", e.g. "7.3 b1.wav Here's a hint." One sentence per clip.
# Needs the VoiceStudio app open (local API on 127.0.0.1:3900). Voice: "Male English".
set -e
HERE=${0:A:h}
VOICE=5460ffd3
n=$1; redo=${3:-}
dir="$HERE/mental-maths-ep$(printf %02d $n)/voice"
[ -f "$dir/cues.txt" ] || { echo "No $dir/cues.txt"; exit 1; }
if ! curl -s -o /dev/null --max-time 3 http://127.0.0.1:3900/engines/tts; then
  open -a VoiceStudio; echo "Started VoiceStudio; waiting for it"; for _ in {1..60}; do sleep 2; curl -s -o /dev/null --max-time 3 http://127.0.0.1:3900/engines/tts && break; done
fi
cd "$dir"
prev_end=0
while read -r start clip text; do
  [[ -z "$start" || "$start" == \#* ]] && continue
  if [[ ! -f "$clip" || "$redo" == all || "$redo.wav" == "$clip" ]]; then
    seed=7; [[ "$redo.wav" == "$clip" ]] && seed=$RANDOM
    python3 -c 'import json,sys;print(json.dumps(dict(model="omnivoice",voice=sys.argv[1],input=sys.argv[2],response_format="wav",seed=int(sys.argv[3]),speed=0.95)))' "$VOICE" "$text" "$seed" \
      | curl -s -f -o raw.wav -H 'Content-Type: application/json' --max-time 400 -d @- http://127.0.0.1:3900/v1/audio/speech \
      || { sleep 3; echo "retrying $clip"; python3 -c 'import json,sys;print(json.dumps(dict(model="omnivoice",voice=sys.argv[1],input=sys.argv[2],response_format="wav",seed=int(sys.argv[3]),speed=0.95)))' "$VOICE" "$text" "$seed" | curl -s -f -o raw.wav -H 'Content-Type: application/json' --max-time 400 -d @- http://127.0.0.1:3900/v1/audio/speech; }
    # trim silence at both ends, 120 ms fade-out so no line ends abruptly
    ffmpeg -v error -y -i raw.wav -af "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,afade=t=in:d=0.02,areverse,afade=t=in:d=0.12,areverse,apad=pad_dur=0.1,aresample=48000" "$clip"
    rm raw.wav
  fi
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$clip")
  end=$(( start + dur ))
  warn=""; (( start < prev_end )) && warn="  OVERLAPS previous line"; (( end > 24 )) && warn="$warn  RUNS PAST 24s"
  printf "%6.2f-%6.2fs  %-7s %s%s\n" $start $end $clip "$text" "$warn"
  prev_end=$end
done < cues.txt
