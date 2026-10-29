#!/bin/zsh
# Makes the voiceover clips from voice/lines.txt ("clip text", one sentence per clip).
# Usage: ./make-voice.sh            (makes missing clips only)
#        ./make-voice.sh --redo h3b (new take of one clip)   ./make-voice.sh --redo all
# Needs VoiceStudio (local API on 127.0.0.1:3900). Voice: "Male English" (5460ffd3), same as Solve it in your head.
set -e
HERE=${0:A:h}
VOICE=5460ffd3
redo=${2:-}
SPEED=${SPEED:-1.05}
if ! curl -s -o /dev/null --max-time 3 http://127.0.0.1:3900/engines/tts; then
  open -a VoiceStudio; echo "Started VoiceStudio; waiting for it"; for _ in {1..60}; do sleep 2; curl -s -o /dev/null --max-time 3 http://127.0.0.1:3900/engines/tts && break; done
fi
cd "$HERE/voice"
while read -r clip text; do
  [[ -z "$clip" || "$clip" == \#* ]] && continue
  if [[ ! -f "$clip.wav" || "$redo" == all || "$redo" == "$clip" ]]; then
    seed=7; [[ "$redo" == "$clip" ]] && seed=$RANDOM
    for attempt in 1 2; do
      python3 -c 'import json,sys;print(json.dumps(dict(model="omnivoice",voice=sys.argv[1],input=sys.argv[2],response_format="wav",seed=int(sys.argv[3]),speed=float(sys.argv[4]))))' "$VOICE" "$text" "$seed" "$SPEED" \
        | curl -s -f -o raw.wav -H 'Content-Type: application/json' --max-time 400 -d @- http://127.0.0.1:3900/v1/audio/speech && break
      sleep 3; echo "retrying $clip"
    done
    # trim silence at both ends, 120 ms fade-out so no line ends abruptly
    ffmpeg -v error -y -i raw.wav -af "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,afade=t=in:d=0.02,areverse,afade=t=in:d=0.12,areverse,apad=pad_dur=0.1,aresample=48000" "$clip.wav"
    rm raw.wav
  fi
  printf "%5.2fs  %-5s %s\n" "$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$clip.wav")" "$clip" "$text"
done < lines.txt
