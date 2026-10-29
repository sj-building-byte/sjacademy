# Checks every voice line in voice/cues.txt is audible at its cue in the final video (waveform match). Run by mental-maths-render.sh.
# Usage: python3 mental-maths-voicecheck.py "<final.mp4>" <episode>/voice   Exits 1 if any line is missing.
import array,math,subprocess,sys
fin,vdir=sys.argv[1],sys.argv[2]
def pcm(args):
    a=array.array('h');a.frombytes(subprocess.run(["ffmpeg","-v","error"]+args+["-ac","1","-ar","8000","-f","s16le","-"],capture_output=True).stdout);return a
missing=0
for line in open(vdir+"/cues.txt"):
    if not line.strip() or line.startswith("#"): continue
    start,clip,text=line.split(" ",2);start=float(start)
    c=pcm(["-i",f"{vdir}/{clip}"]);x=pcm(["-ss",str(max(0,start-0.05)),"-t",str(len(c)/8000+0.2),"-i",fin])
    n=min(len(c),len(x)-500);best=0
    for l in range(320,481,2):
        num=sum(x[i+l]*c[i] for i in range(0,n,3));den=math.sqrt(sum(x[i+l]**2 for i in range(0,n,3))*sum(c[i]**2 for i in range(0,n,3)))+1
        best=max(best,num/den)
    missing+=best<=0.6
    print(f"  {start:5.2f}s {clip:7s} match {best:.2f}  {'OK' if best>0.6 else 'MISSING'}  {text.strip()}")
sys.exit(1 if missing else 0)
