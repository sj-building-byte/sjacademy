import math
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@400;500&family=Caveat:wght@500&display=block">'
BASE='''<!doctype html><meta charset=utf-8>'''+FONTS+'''<style>*{box-sizing:border-box;margin:0}html,body{width:1080px;height:1920px;overflow:hidden;background:#070a0b}
.f{position:relative;width:1080px;height:1920px;overflow:hidden;color:#eef0ea;font-family:"Instrument Serif",Georgia,serif}
.q{position:absolute;left:84px;width:840px;font-size:108px;line-height:1.02;letter-spacing:-.012em}
.src{position:absolute;left:88px;font:500 33px/1.32 "IBM Plex Mono",monospace;letter-spacing:.01em;color:#b9c3bf}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}</style><div class=f>'''
# 1 hook
f1=BASE+"""<img class=bg src="bg_arm.png"><div style="position:absolute;left:0;right:0;top:760px;bottom:0;background:linear-gradient(180deg,rgba(6,9,10,0),rgba(6,9,10,.9) 22%,rgba(6,9,10,.96))"></div>
<div class=q style="top:850px;font-size:66px;line-height:1.1">Unrealistic solutions are also not given credit, e.g.</div>
<div class=q style="top:1006px;font-size:146px;line-height:.98;color:#ff5a4d">‘robotic arm’</div>
<div class=q style="top:1150px;font-size:66px;line-height:1.1">or ‘mechanical hand’.</div>
<div class=src style="top:1244px">Cambridge examiner report<br>A Level Physics, November 2022</div></div>"""
# 2 burette
f2=BASE+'''<img class=bg src="bg_burette.png"><div style="position:absolute;left:0;right:0;top:900px;bottom:0;background:linear-gradient(180deg,rgba(6,9,10,0),rgba(6,9,10,.88) 20%,rgba(6,9,10,.95))"></div>
<svg class=bg viewBox="0 0 1080 1920"><path d="M238 690 H420" stroke="#eef0ea" stroke-width="2.5"/><circle cx="238" cy="690" r="9" fill="none" stroke="#eef0ea" stroke-width="2.5"/></svg>
<div class=src style="left:432px;top:668px;color:#fff;font-size:38px">nearest 0.05 cm³</div>
<div class=q style="top:960px;font-size:92px;line-height:1.04">Some did not read the burette to the expected level of accuracy.</div><div class=src style="top:1272px">Cambridge examiner report<br>A Level Chemistry, November 2023</div></div>'''
# 3 wall
rows=''
for i in range(30):
    x=-6+(i*37%23); r=(-.5+(i*13%10)/10)*1.4
    rows+=f'<div style="position:absolute;left:{70+x}px;top:{40+i*63}px;transform:rotate({r}deg);font:500 70px/1 Caveat,cursive;color:#20262c;white-space:nowrap">turns limewater milky</div>'
lines=''.join(f'<div style="position:absolute;left:0;right:0;top:{98+i*63}px;height:2px;background:#b9c9d4"></div>' for i in range(30))
f3=BASE+f'''<div class=bg style="background:#ebe8df"></div>{lines}{rows}<div style="position:absolute;left:0;right:0;top:760px;height:640px;background:#090c0d"></div>
<div class=q style="top:806px;font-size:96px">Not only was this impossible, but ‘milky’ is not an allowed description</div><div class=src style="top:1218px">Cambridge examiner report<br>A Level Chemistry, June 2022</div></div>'''
# 4 drop
f4=BASE+'''<img class=bg src="bg_drop.png"><div style="position:absolute;left:0;right:0;top:0;height:900px;background:linear-gradient(180deg,rgba(8,4,8,.5),rgba(8,4,8,0))"></div>
<div style="position:absolute;left:0;right:0;top:760px;height:640px;background:radial-gradient(ellipse at 74% 50%,rgba(6,4,6,.86),rgba(6,4,6,0) 68%)"></div><div class=q style="top:900px;font-size:158px;line-height:.92;font-style:italic;left:500px;width:540px;color:#fff">Do it again.</div></div>'''
# 5 end
f5=BASE+"""<div class=bg style="background:#070a0b"></div><img src="logo.svg" style="position:absolute;left:78px;top:290px;width:560px">
<div class=q style="top:500px;font-size:118px;line-height:.98">Robotic arms not provided.</div>
<div style="position:absolute;left:84px;top:800px;width:840px;font:500 38px/1.45 'IBM Plex Mono',monospace;color:#eef0ea">A Level lab practicals<br><span style="color:#b9c3bf">Physics, Chemistry, Biology</span></div>
<div class=q style="top:950px;font-size:64px;line-height:1.08">Message us before your practical.</div>
<div style="position:absolute;left:84px;top:1120px;font:500 44px/1.28 'IBM Plex Mono',monospace;color:#FCE004">sjacademy.pk<br>@sjacademypk</div></div>"""
for n,h in zip(['1-hook','2-burette','3-parallax','4-drop','5-end'],[f1,f2,f3,f4,f5]): open(n+'.html','w').write(h)
