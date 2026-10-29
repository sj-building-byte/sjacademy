#!/bin/bash
# Builds the minimal SFX set and the ducked 20s music bed for the v3 film.
set -e
Q="-loglevel error -y"
mkdir -p assets/sfx3
ffmpeg $Q -f lavfi -i "anoisesrc=d=0.4:c=pink:r=44100:a=0.6:seed=11" -af "highpass=f=1800,lowpass=f=7000,tremolo=f=34:d=0.7,afade=t=in:d=0.03,afade=t=out:st=0.18:d=0.22,volume=0.9" assets/sfx3/pen.wav
ffmpeg $Q -f lavfi -i "anoisesrc=d=0.5:c=white:r=44100:a=0.5:seed=7" -af "bandpass=f=2600:w=1800,afade=t=in:d=0.18,afade=t=out:st=0.22:d=0.28,volume=0.7" assets/sfx3/swipe.wav
ffmpeg $Q -f lavfi -i "anoisesrc=d=0.7:c=brown:r=44100:a=0.7:seed=3" -f lavfi -i "anoisesrc=d=0.7:c=white:r=44100:a=0.25:seed=5" -filter_complex "[0][1]amix=inputs=2:normalize=0,highpass=f=250,lowpass=f=6000,tremolo=f=9:d=0.5,afade=t=in:d=0.12,afade=t=out:st=0.3:d=0.4,volume=1.2" assets/sfx3/pageturn.wav
ffmpeg $Q -f lavfi -i "aevalsrc='0.9*sin(2*PI*(95-40*t)*t)*exp(-16*t)':d=0.4:s=44100" -f lavfi -i "anoisesrc=d=0.4:c=pink:r=44100:a=0.4:seed=9" -filter_complex "[1]lowpass=f=1500,afade=t=out:st=0:d=0.08[n];[0][n]amix=inputs=2:normalize=0" assets/sfx3/stamp.wav
ffmpeg $Q -f lavfi -i "aevalsrc='0.6*sin(2*PI*1800*t)*exp(-90*t)+0.3*sin(2*PI*900*t)*exp(-60*t)':d=0.2:s=44100" assets/sfx3/tap.wav
ffmpeg $Q -i assets/audio/musicgen-soothing-raw.wav -af "atempo=0.99200,atrim=start=0.387,asetpts=PTS-STARTPTS,atrim=duration=20,afade=t=in:d=0.05,afade=t=out:st=18.2:d=1.8,loudnorm=I=-18:TP=-2:LRA=11,aresample=44100" -ac 2 assets/audio/bgm-base.wav
DUCK=$(python3 - <<'PY'
hits=[(1.3,.5),(3.25,.4),(4.45,.4),(4.95,.4),(7.05,.2),(7.55,.2),(8.85,.5),(9.2,.4),(10.95,.7),(11.9,.4),(16.75,.4)]
m=None
for s,d in hits:
    t=f"clip((t-{s-0.06:.2f})/0.06\\,0\\,1)*clip(({s+d+0.12:.2f}-t)/0.12\\,0\\,1)"
    m=t if m is None else f"max({m}\\,{t})"
print(f"volume='1-0.55*{m}':eval=frame")
PY
)
ffmpeg $Q -i assets/audio/bgm-base.wav -af "$DUCK" assets/audio/bgm20.wav
