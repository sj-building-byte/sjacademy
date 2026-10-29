#!/bin/zsh
# Renders "Solve it in your head" episodes, normalises them to -14 LUFS and puts them in Finished.
# Usage: ./mental-maths-render.sh 5        (one episode)
#        ./mental-maths-render.sh 5 6 7    (several)
# Run only after the episode has passed 00 Start Here/ACCURACY.md.
set -e
HERE=${0:A:h}
FIN="$HOME/Documents/SJ Academy/✅ Finished/Videos/Solve it in your head"
mkdir -p "$FIN"
for n in "$@"; do
  dir="$HERE/mental-maths-ep$(printf %02d $n)"
  [ -d "$dir" ] || { echo "No project for episode $n: $dir"; exit 1; }
  cd "$dir"
  npx --yes hyperframes@0.8.167 check 2>&1 | grep -q "Check passed" || { echo "Episode $n fails hyperframes check"; exit 1; }
  npx --yes hyperframes@0.8.167 render -o renders/tmp.mp4 >/dev/null 2>&1
  if [ -f voice/cues.txt ]; then
    # Voiceover (from #8): each line of voice/cues.txt is "start clip text". Desk sounds drop to 0.55 under the voice.
    ins=(-i renders/tmp.mp4); fc="[0:a]volume=0.55[bg];"; labels=""; i=1
    while read -r start clip rest; do
      [[ -z "$start" || "$start" == \#* ]] && continue
      ins+=(-i "voice/$clip"); fc+="[${i}:a]aresample=48000,adelay=$(printf %.0f $(( start * 1000 ))):all=1[v$i];"; labels+="[v$i]"; i=$((i + 1))
    done < voice/cues.txt
    fc+="${labels}amix=inputs=$((i - 1)):normalize=0,highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=120[vo];[bg][vo]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    ffmpeg -v error -y "${ins[@]}" -filter_complex "$fc" -map 0:v -map "[a]" -c:v copy -ar 48000 -c:a aac -b:a 192k "$FIN/Solve it in your head $n.mp4"
    python3 "$HERE/mental-maths-voicecheck.py" "$FIN/Solve it in your head $n.mp4" voice || { echo "Episode $n: voice lines missing from the final, see above"; exit 1; }
  else
    ffmpeg -v error -y -i renders/tmp.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k "$FIN/Solve it in your head $n.mp4"
  fi
  rm renders/tmp.mp4
  lufs=$(ffmpeg -i "$FIN/Solve it in your head $n.mp4" -af ebur128 -f null - 2>&1 | grep -E '^\s+I:' | tail -1 | tr -s ' ')
  echo "Episode $n -> $FIN/Solve it in your head $n.mp4 ($lufs)"
done
