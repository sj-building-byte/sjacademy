# Builds the "10 Hacks" video from episode.py and the voice clips in voice/.
# Writes index.html, compositions/*.html and timing.json. Run: python3 build.py
# v2 look (26 Oct 2026): navy gradient ground, drifting chalk-maths layer, one accent colour per hack,
# full-screen number hit between hacks. v1 (brown) is in archive/v1-brown/. Voice: ./make-voice.sh first.
import json, os, subprocess, html

HERE = os.path.dirname(os.path.abspath(__file__))
W, H_ = 1080, 1920
NAVY, NAVY2, INK = "#0A0F2C", "#151C52", "#F7F6FF"
YELLOW, ORANGE = "#FCE004", "#FE6100"
DIM = "rgba(247,246,255,0.55)"
# one accent per hack: notes, arrows, glows, the transition panel
ACC = ["#22D3EE", "#FF4D6D", "#A78BFA", "#34D399", "#FB923C", "#F472B6", "#60A5FA", "#2DD4BF", "#FF6B6B", "#C084FC"]
GOLD = f"linear-gradient(135deg,{YELLOW} 0%,#FFC21A 55%,{ORANGE} 100%)"
METRICS = json.load(open(os.path.join(HERE, "assets/brand/poppins-metrics.json")))
X0 = 90
HIT = 0.6           # seconds each full-screen number hit adds before a hack
BOARD_DX, BOARD_DY = 30, 200   # episode.py board coordinates -> inside the card
LOGO_TOP, LOGO_W = 280, 230
COUNT_TOP, COUNT_PX = 440, 230
CARD = dict(x=80, y=880, w=920, h=510)
CAP_BOTTOM = 340

def shade(hex_, f):
    h = hex_.lstrip("#")
    return "#" + "".join(f"{int(int(h[i:i + 2], 16) * f):02X}" for i in (0, 2, 4))

def rgba(hex_, a):
    h = hex_.lstrip("#")
    return f"rgba({int(h[0:2], 16)},{int(h[2:4], 16)},{int(h[4:6], 16)},{a})"

# ---------------------------------------------------------------- measuring and board items
def tw(s, size, weight=700):
    m = METRICS[str(weight)]
    return sum(m.get(c, 600) for c in s) / 1000 * size

def text(id, s, x, y, size, weight=700, tone="ink"):
    w = tw(s, size, weight)
    return dict(kind="t", id=id, s=s, x=x, y=y, size=size, weight=weight, tone=tone, w=w,
                x1=(x or 0) + w)

def row(y, size, parts, x=X0, weight=700):
    out = []
    for id, s in parts:
        it = text(id, s, x, y, size, weight)
        out.append(it)
        x = it["x1"]
    return out

def frac(p, num, den, x, y, size):
    wn, wd = tw(num, size), tw(den, size)
    w = max(wn, wd) + size * 0.3
    off = size * 0.7
    n = text(p + "n", num, x + (w - wn) / 2, y - off, size)
    d = text(p + "d", den, x + (w - wd) / 2, y + off, size)
    bar = dict(kind="bar", id=p + "bar", x=x, y=y, w=w, x1=x + w, size=size)
    return [n, d, bar]

def note(id, s, x, y, size=54):
    return dict(kind="note", id=id, s=s, x=x, y=y, size=size, w=len(s) * size * 0.42)

def arrow(id, x, y, w):
    return dict(kind="arrow", id=id, x=x, y=y, w=w, d=f"M0 30 L{w} 30 M{w - 26} 8 L{w} 30 L{w - 26} 52",
                length=w + 70)

def path(id, d, length, width=7):
    return dict(kind="path", id=id, d=d, length=length, width=width)

# ---------------------------------------------------------------- voice
def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", f]).decode().strip())

def voice_lines():
    lines = {}
    for ln in open(os.path.join(HERE, "voice/lines.txt")):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        clip, t = ln.split(" ", 1)
        lines[clip] = dict(text=t, dur=dur(os.path.join(HERE, f"voice/{clip}.wav")))
    return lines

# ---------------------------------------------------------------- shared css
def fonts():
    return "\n".join(
        [f"@font-face{{font-family:'SJ Poppins';font-weight:{w};src:url('assets/brand/Poppins-{n}.ttf')}}"
         for w, n in [(500, "Medium"), (600, "SemiBold"), (700, "Bold"), (800, "ExtraBold")]]
        + ["@font-face{font-family:'SJ Caveat';font-weight:600;src:url('assets/brand/Caveat-600.woff2')}"])

BASE_CSS = f"""
#root{{position:absolute;inset:0;font-family:'SJ Poppins';color:{INK};font-kerning:none;}}
.tk{{position:absolute;white-space:pre;line-height:1.2;z-index:2;text-shadow:0 6px 30px rgba(10,15,44,0.55);}}
.note{{position:absolute;white-space:pre;font-family:'SJ Caveat';font-weight:600;line-height:1.2;z-index:2;}}
.box{{position:absolute;background:{GOLD};border-radius:16px;z-index:1;transform-origin:50% 50%;
  box-shadow:0 14px 50px rgba(252,200,4,0.45),inset 0 2px 0 rgba(255,255,255,0.5);}}
.ring{{position:absolute;border:4px solid {YELLOW};border-radius:22px;z-index:1;transform-origin:50% 50%;}}
.bar{{position:absolute;height:7px;border-radius:4px;background:{INK};z-index:2;}}
svg.pen{{position:absolute;left:0;top:0;overflow:visible;z-index:2;}}
.gold{{background:{GOLD};-webkit-background-clip:text;background-clip:text;color:transparent;}}
.hl{{background-image:{GOLD};background-repeat:no-repeat;background-size:0% 100%;padding:0 10px;border-radius:10px;
  -webkit-box-decoration-break:clone;box-decoration-break:clone;}}
"""

def esc(s):
    return html.escape(s, quote=True)

def words(s, cls="w"):
    return " ".join(f'<span class="{cls}">{esc(w)}</span>' for w in s.split(" "))

# ---------------------------------------------------------------- hack scene
def hack_scene(k, hk, V, clips):
    cid = f"h{k:02d}"
    P = cid + "-"
    acc = ACC[k - 1]
    a, b = clips
    t_a = 0.45
    t_b = t_a + V[a]["dur"] + 0.22
    D = round(t_b + V[b]["dur"] + 0.8, 3)
    anchors = {"a": (t_a, V[a]["dur"]), "b": (t_b, V[b]["dur"])}

    def at(t):
        if isinstance(t, tuple):
            s, d = anchors[t[0]]
            return round(s + t[1] * d, 3)
        return t

    items = {it["id"]: it for it in hk["items"]}
    body, js, sfx = [], [], []
    state = {i: dict(op=0.0, col=INK if it.get("tone") != "dim" else DIM) for i, it in items.items()}

    # title, divider, rule, card
    rule_html = "".join(
        f'<span class="{"hl" if h else "rw"}" id="{P}r{j}">{esc(s)}</span>' for j, (s, h) in enumerate(hk["rule"]))
    tw_ = hk["title"].split(" ")
    title_html = " ".join(f'<span class="m"><span class="w" id="{P}tw{j}">{esc(w)}</span></span>' for j, w in enumerate(tw_))
    js.append(f"tl.fromTo('#{P}title .w',{{yPercent:110,rotation:6}},{{yPercent:0,rotation:0,duration:0.45,ease:'expo.out',stagger:0.07}},0.05);")
    js.append(f"tl.fromTo('#{P}div',{{scaleX:0}},{{scaleX:1,duration:0.6,ease:'expo.inOut'}},0.1);")
    js.append(f"tl.fromTo('#{P}rule',{{opacity:0,y:24,filter:'blur(8px)'}},{{opacity:1,y:0,filter:'blur(0px)',duration:0.35,ease:'power3.out'}},0.22);")
    js.append(f"tl.fromTo('#{P}card',{{opacity:0,scale:0.9,y:60}},{{opacity:1,scale:1,y:0,duration:0.55,ease:'back.out(1.4)'}},0.18);")
    js.append(f"tl.fromTo('#{P}cardglow',{{opacity:0}},{{opacity:1,duration:0.8,ease:'sine.out'}},0.3);")

    for it in hk["items"]:
        i = P + it["id"]
        if it["kind"] == "t":
            col = state[it["id"]]["col"]
            body.append(f'<div class="tk" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - it["size"] * 0.6:.1f}px;'
                        f'font-size:{it["size"]}px;font-weight:{it["weight"]};color:{col}">{esc(it["s"])}</div>')
        elif it["kind"] == "note":
            body.append(f'<div class="note" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - it["size"] * 0.62:.1f}px;'
                        f'font-size:{it["size"]}px;color:{acc}">{esc(it["s"])}</div>')
        elif it["kind"] == "bar":
            body.append(f'<div class="bar" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - 3:.1f}px;width:{it["w"]:.1f}px"></div>')
        elif it["kind"] == "arrow":
            body.append(f'<svg class="pen" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - 30:.1f}px" width="{it["w"]:.0f}" height="60">'
                        f'<path id="{i}-p" d="{it["d"]}" fill="none" stroke="{acc}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
        elif it["kind"] == "path":
            body.append(f'<svg class="pen" id="{i}" width="{W}" height="{H_}"><path id="{i}-p" d="{it["d"]}" fill="{rgba(acc, 0.12)}" '
                        f'stroke="{INK}" stroke-width="{it["width"]}" stroke-linecap="round" stroke-linejoin="round"/></svg>')
        js.append(f"tl.set('#{i}',{{opacity:0}},0);")
        if it["kind"] in ("arrow", "path"):
            js.append(f"tl.set('#{i}-p',{{strokeDasharray:{it['length']},strokeDashoffset:{it['length']}}},0);")

    def fade(ids, t, to, dur_=0.4):
        for x in ids:
            fr = state[x]["op"]
            if to > fr:
                js.append(f"tl.fromTo('#{P}{x}',{{opacity:{fr},y:46,scale:0.86,filter:'blur(10px)'}},{{opacity:{to},y:0,scale:1,filter:'blur(0px)',duration:{dur_},ease:'back.out(1.8)'}},{t});")
            else:
                js.append(f"tl.fromTo('#{P}{x}',{{opacity:{fr}}},{{opacity:{to},duration:0.3,ease:'power2.out'}},{t});")
            state[x]["op"] = to

    nbox = 0
    hl_rule_t = None
    shown = set()
    for ev in hk["events"]:
        t, act = at(ev[0]), ev[1]
        tgt = ev[2] if len(ev) > 2 else []
        shown.update([tgt] if isinstance(tgt, str) else list(tgt))
        if act == "in":
            for j, x in enumerate(ev[2]):
                fade([x], round(t + j * 0.07, 3), 1)
            sfx.append(("fx-pop", t + 0.05))
        elif act == "dim":
            fade(ev[2], t, 0.3)
        elif act == "out":
            for x in ev[2]:
                js.append(f"tl.fromTo('#{P}{x}',{{opacity:{state[x]['op']},scale:1,filter:'blur(0px)'}},{{opacity:0,scale:1.4,filter:'blur(8px)',duration:0.22,ease:'expo.in'}},{t});")
                state[x]["op"] = 0
        elif act in ("from", "swap"):
            pairs = [(ev[2], ev[3])] if act == "from" else list(ev[2].items())
            if act == "swap":
                for src in ev[2].values():
                    js.append(f"tl.fromTo('#{P}{src}',{{opacity:1}},{{opacity:0,duration:0.06}},{t});")
                    state[src]["op"] = 0
            for dst, src in pairs:
                d, s = items[dst], items[src]
                sc = s["size"] / d["size"]
                dx, dy = s["x"] - d["x"], s["y"] - d["y"]
                lift = -80 if act == "swap" and dx < 0 else (80 if act == "swap" else -40)
                js.append(f"tl.set('#{P}{dst}',{{opacity:1,transformOrigin:'0% 50%'}},{t});")
                js.append(f"tl.fromTo('#{P}{dst}',{{x:{dx:.1f},scale:{sc:.3f}}},{{x:0,scale:1,duration:0.62,ease:'power3.inOut'}},{t});")
                js.append(f"tl.fromTo('#{P}{dst}',{{y:{dy:.1f}}},{{y:{lift},duration:0.31,ease:'power2.out'}},{t});")
                js.append(f"tl.to('#{P}{dst}',{{y:0,duration:0.31,ease:'power2.in'}},{t + 0.31:.3f});")
                js.append(f"tl.fromTo('#{P}{dst}',{{color:'{acc}'}},{{color:'{state[dst]['col']}',duration:0.5,ease:'sine.in'}},{t + 0.3:.3f});")
                state[dst]["op"] = 1
            sfx.append(("fx-pop", t + 0.55))
        elif act == "drop":
            x = ev[2]
            js.append(f"tl.fromTo('#{P}{x}',{{opacity:0,y:-140,scale:1.5,color:'{acc}'}},{{opacity:1,y:0,scale:1,duration:0.42,ease:'bounce.out'}},{t});")
            js.append(f"tl.to('#{P}{x}',{{color:'{state[x]['col']}',duration:0.4}},{t + 0.5:.3f});")
            state[x]["op"] = 1
            sfx.append(("fx-pop", t + 0.2))
        elif act == "note":
            x = ev[2]
            js.append(f"tl.fromTo('#{P}{x}',{{opacity:1,rotation:-3,clipPath:'inset(0% 100% 0% 0%)'}},{{rotation:-3,clipPath:'inset(0% 0% 0% 0%)',duration:0.45,ease:'sine.inOut'}},{t});")
            state[x]["op"] = 1
        elif act == "draw":
            x = ev[2]
            ln = items[x]["length"]
            js.append(f"tl.set('#{P}{x}',{{opacity:1}},{t});")
            js.append(f"tl.fromTo('#{P}{x}-p',{{strokeDashoffset:{ln}}},{{strokeDashoffset:0,duration:{0.33 if items[x]['kind'] == 'arrow' else 0.6},ease:'sine.inOut'}},{t});")
            state[x]["op"] = 1
        elif act == "hl_rule":
            hl_rule_t = t
            js.append(f"tl.fromTo('#{P}rule .hl',{{backgroundSize:'0% 100%',color:'{INK}'}},{{backgroundSize:'100% 100%',color:'{NAVY}',duration:0.35,ease:'power2.out'}},{t});")
            sfx.append(("sj-sfx-highlighter-swipe", t))
        elif act == "stamp":
            ids = ev[2]
            its = [items[x] for x in ids]
            x0 = min(i_["x"] for i_ in its) - 22
            x1 = max(i_["x1"] for i_ in its) + 22
            y0 = min(i_["y"] - i_["size"] * 0.62 for i_ in its) - 6
            y1 = max(i_["y"] + i_["size"] * 0.55 for i_ in its) + 6
            bid, rid = f"{P}box{nbox}", f"{P}ring{nbox}"
            nbox += 1
            geo = f"left:{x0:.1f}px;top:{y0:.1f}px;width:{x1 - x0:.1f}px;height:{y1 - y0:.1f}px"
            body.append(f'<div class="box" id="{bid}" style="{geo}"></div>')
            body.append(f'<div class="ring" id="{rid}" style="left:{x0 - 6:.1f}px;top:{y0 - 6:.1f}px;width:{x1 - x0 + 12:.1f}px;height:{y1 - y0 + 12:.1f}px"></div>')
            js.append(f"tl.set('#{bid},#{rid}',{{opacity:0}},0);")
            js.append(f"tl.fromTo('#{bid}',{{opacity:0,scale:1.45,rotation:-9}},{{opacity:1,scale:1,rotation:-1.5,duration:0.18,ease:'back.out(2)'}},{t});")
            js.append(f"tl.fromTo('#{bid}',{{x:3}},{{x:0,duration:0.14,ease:'steps(4)'}},{t + 0.18:.3f});")
            js.append(f"tl.fromTo('#{rid}',{{opacity:0.95,scale:1}},{{opacity:0,scale:1.45,duration:0.6,ease:'expo.out'}},{t + 0.12:.3f});")
            for x in ids:
                if items[x]["kind"] == "bar":
                    js.append(f"tl.fromTo('#{P}{x}',{{backgroundColor:'{INK}'}},{{backgroundColor:'{NAVY}',duration:0.05}},{t + 0.04:.3f});")
                else:
                    if state[x]["op"] < 1:
                        js.append(f"tl.fromTo('#{P}{x}',{{opacity:{state[x]['op']}}},{{opacity:1,duration:0.08}},{t});")
                        state[x]["op"] = 1
                    js.append(f"tl.fromTo('#{P}{x}',{{color:'{state[x]['col']}',textShadow:'0 6px 30px rgba(10,15,44,0.55)'}},{{color:'{NAVY}',textShadow:'0 0px 0px rgba(10,15,44,0)',duration:0.05}},{t + 0.04:.3f});")
                    state[x]["col"] = NAVY
            sfx.append(("sj-sfx-stamp", t + 0.03))
        else:
            raise SystemExit(f"{cid}: unknown action {act}")

    never = [i for i in items if i not in shown]
    if never:
        raise SystemExit(f"{cid}: never appears: {never}")
    # exit: the stage pushes toward camera as the next hit panel sweeps over it
    js.append(f"tl.fromTo('#{P}stage',{{scale:1,opacity:1,filter:'blur(0px)'}},{{scale:1.08,opacity:0,filter:'blur(12px)',duration:0.3,ease:'expo.in'}},{D - 0.3:.3f});")

    c = CARD
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#{P}stage{{position:absolute;inset:0;transform-origin:50% 55%;}}
#{P}title{{position:absolute;left:470px;top:{COUNT_TOP + 70}px;width:520px;font-size:84px;font-weight:800;line-height:1.05;letter-spacing:-0.02em;white-space:nowrap;}}
#{P}title .m{{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:6px;}}
#{P}title .w{{display:inline-block;}}
#{P}div{{position:absolute;left:100px;top:{COUNT_TOP + COUNT_PX + 30}px;width:880px;height:4px;border-radius:2px;
  background:linear-gradient(90deg,{YELLOW},{acc} 60%,{rgba(acc, 0)});transform-origin:0% 50%;}}
#{P}rule{{position:absolute;left:100px;top:{COUNT_TOP + COUNT_PX + 60}px;width:880px;font-size:42px;font-weight:500;line-height:1.4;color:rgba(247,246,255,0.88);}}
#{P}rule .hl{{font-weight:700;}}
#{P}card{{position:absolute;left:{c['x']}px;top:{c['y']}px;width:{c['w']}px;height:{c['h']}px;border-radius:40px;
  background:linear-gradient(160deg,rgba(40,48,110,0.78),rgba(14,19,58,0.86));border:2px solid rgba(255,255,255,0.14);
  box-shadow:0 30px 80px rgba(3,6,24,0.55);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);overflow:hidden;}}
#{P}cardglow{{position:absolute;right:-180px;bottom:-220px;width:620px;height:620px;border-radius:50%;
  background:radial-gradient(circle,{rgba(acc, 0.32)},{rgba(acc, 0)} 70%);}}
#{P}board{{position:absolute;left:{BOARD_DX}px;top:{BOARD_DY}px;width:{W}px;height:{H_}px;}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="{P}stage" data-layout-allow-overlap>
      <div id="{P}card"><div id="{P}cardglow"></div></div>
      <div class="title" id="{P}title">{title_html}</div>
      <div id="{P}div"></div>
      <div class="rule" id="{P}rule">{rule_html}</div>
      <div id="{P}board" data-layout-allow-overlap>
      {chr(10).join("        " + b_ for b_ in body).strip()}
      </div>
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join("    " + j for j in js).strip()}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, D, html_, [(a, t_a), (b, t_b)], sfx, hl_rule_t

# ---------------------------------------------------------------- intro, recap, end card
def intro_scene(spec, V):
    cid = "intro"
    t_v = 0.3
    D = round(t_v + V[spec["voice"]]["dur"] + 0.55, 3)
    tick = esc(spec["ticker"] * 3)
    t1, t2 = spec["title"]
    tick_w = tw(spec["ticker"], 44, 700)
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#in-logo{{position:absolute;left:100px;top:{LOGO_TOP}px;width:{LOGO_W}px;}}
#in-big{{position:absolute;left:70px;top:380px;font-size:520px;font-weight:800;line-height:1;letter-spacing:-0.06em;padding-right:30px;
  filter:drop-shadow(0 20px 60px rgba(252,180,4,0.35));transform-origin:30% 60%;}}
#in-chip{{position:absolute;left:620px;top:560px;font-size:34px;font-weight:700;letter-spacing:0.18em;color:{NAVY};background:{ACC[0]};
  padding:10px 24px;border-radius:40px;transform-origin:0% 50%;}}
#in-chip2{{position:absolute;left:620px;top:650px;font-family:'SJ Caveat';font-size:60px;font-weight:600;color:{ACC[1]};}}
#in-title{{position:absolute;left:100px;top:930px;font-size:128px;font-weight:800;line-height:1;letter-spacing:-0.03em;white-space:nowrap;}}
#in-title .m{{display:inline-block;overflow:hidden;vertical-align:top;padding:0 0 14px;}}
#in-title .w{{display:inline-block;}}
#in-sub{{position:absolute;left:100px;top:1105px;font-size:44px;font-weight:500;color:rgba(247,246,255,0.86);}}
#in-sub .w{{display:inline-block;}}
#in-band{{position:absolute;left:-60px;top:1240px;width:1200px;height:96px;background:linear-gradient(90deg,{ACC[2]},{ACC[1]} 50%,{ORANGE});
  transform:rotate(-4deg);overflow:hidden;box-shadow:0 20px 60px rgba(3,6,24,0.5);}}
#in-tick{{position:absolute;left:0;top:18px;font-size:44px;font-weight:700;white-space:nowrap;color:{NAVY};}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="in-stage">
      <img id="in-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
      <div id="in-big" class="gold">{esc(spec["big"])}</div>
      <div id="in-chip">O &amp; A LEVEL</div>
      <div id="in-chip2">save this one</div>
      <div id="in-title"><span class="m"><span class="w">{esc(t1.strip())}</span></span> <span class="m"><span class="w"><span id="in-hl" class="hl">{esc(t2)}</span></span></span></div>
      <div id="in-sub">{words(spec["sub"])}</div>
      <div id="in-band" data-layout-allow-overflow data-layout-ignore><div id="in-tick">{tick}</div></div>
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#in-logo',{{opacity:0,y:-20}},{{opacity:1,y:0,duration:0.5,ease:'power3.out'}},0.05);
    tl.fromTo('#in-big',{{scale:2.4,opacity:0,rotation:-8}},{{scale:1,opacity:1,rotation:0,duration:0.5,ease:'expo.out'}},0);
    tl.fromTo('#in-big',{{x:-10}},{{x:0,duration:0.24,ease:'steps(5)'}},0.32);
    tl.fromTo('#in-chip',{{scale:0,rotation:-12}},{{scale:1,rotation:-4,duration:0.45,ease:'back.out(2.2)'}},0.4);
    tl.fromTo('#in-chip2',{{clipPath:'inset(0% 100% 0% 0%)',rotation:-6}},{{clipPath:'inset(0% 0% 0% 0%)',rotation:-6,duration:0.5,ease:'sine.inOut'}},0.75);
    tl.fromTo('#in-title .w',{{yPercent:110}},{{yPercent:0,duration:0.5,ease:'expo.out',stagger:0.1}},0.2);
    tl.fromTo('#in-hl',{{backgroundSize:'0% 100%',color:'{INK}'}},{{backgroundSize:'100% 100%',color:'{NAVY}',duration:0.35,ease:'power2.out'}},0.6);
    tl.fromTo('#in-sub .w',{{opacity:0,y:20,filter:'blur(6px)'}},{{opacity:1,y:0,filter:'blur(0px)',duration:0.3,ease:'power3.out',stagger:0.07}},0.8);
    tl.fromTo('#in-band',{{xPercent:-110}},{{xPercent:0,duration:0.6,ease:'expo.out'}},0.5);
    tl.fromTo('#in-tick',{{x:0}},{{x:-{tick_w:.0f},duration:{D},ease:'none'}},0);
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, D, html_, [(spec["voice"], t_v)], [("fx-impact", 0.12), ("sj-sfx-highlighter-swipe", 0.6), ("fx-whoosh", 0.45)]

def recap_scene(spec, V):
    cid = "recap"
    t_v = 0.45
    D = round(t_v + V[spec["voice"]]["dur"] + 1.7, 3)
    rows = []
    for j, r in enumerate(spec["rows"]):
        assert tw(r, 34, 500) < 740, r
        rows.append(f'<div class="rr" id="rc-r{j}"><span class="rn" style="background:{ACC[j]}">{j + 1:02d}</span><span class="rt">{esc(r)}</span></div>')
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#rc-logo{{position:absolute;left:100px;top:{LOGO_TOP}px;width:{LOGO_W}px;}}
#rc-title{{position:absolute;left:100px;top:400px;font-size:84px;font-weight:800;letter-spacing:-0.02em;white-space:nowrap;}}
#rc-card{{position:absolute;left:80px;top:540px;width:920px;height:800px;border-radius:40px;
  background:linear-gradient(160deg,rgba(40,48,110,0.78),rgba(14,19,58,0.86));border:2px solid rgba(255,255,255,0.14);
  box-shadow:0 30px 80px rgba(3,6,24,0.55);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);}}
#rc-list{{position:absolute;left:120px;top:580px;width:840px;}}
.rr{{font-size:34px;font-weight:500;line-height:1;height:72px;display:flex;align-items:center;white-space:nowrap;border-bottom:2px solid rgba(255,255,255,0.08);}}
.rn{{display:inline-flex;align-items:center;justify-content:center;width:62px;height:46px;margin-right:26px;border-radius:14px;font-size:28px;font-weight:800;color:{NAVY};}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <img id="rc-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
    <div id="rc-title">Your <span id="rc-hl" class="hl">cheat sheet</span></div>
    <div id="rc-card"></div>
    <div id="rc-list">
      {chr(10).join("      " + r for r in rows).strip()}
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#rc-title',{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.45,ease:'expo.out'}},0.05);
    tl.fromTo('#rc-card',{{opacity:0,scale:0.92,y:60}},{{opacity:1,scale:1,y:0,duration:0.55,ease:'back.out(1.4)'}},0.1);
    tl.fromTo('.rr',{{opacity:0,x:-60}},{{opacity:1,x:0,duration:0.45,ease:'expo.out',stagger:0.07}},0.3);
    tl.fromTo('.rn',{{scale:0,rotation:-20}},{{scale:1,rotation:0,duration:0.4,ease:'back.out(2.5)',stagger:0.07}},0.32);
    tl.fromTo('#rc-hl',{{backgroundSize:'0% 100%',color:'{INK}'}},{{backgroundSize:'100% 100%',color:'{NAVY}',duration:0.35,ease:'power2.out'}},0.95);
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, D, html_, [(spec["voice"], t_v)], [("sj-sfx-highlighter-swipe", 0.95)]

def end_scene(spec, V):
    cid = "endcard"
    t_v = 0.5
    t_logo = round(t_v + V[spec["voice"]]["dur"] + 0.2, 3)
    D = round(t_logo + 3.6, 3)
    l1, l2 = spec["lines"]
    syms = [("π", 820, 330, 200, -12), ("√", 860, 1420, 220, 10), ("÷", 120, 1500, 160, -8), ("∑", 760, 980, 180, 8),
            ("%", 140, 1180, 120, 14), ("×", 900, 700, 140, -6)]
    sym_html = "".join(f'<div class="es" style="left:{x}px;top:{y}px;font-size:{s}px;transform:rotate({r}deg)">{c}</div>' for c, x, y, s, r in syms)
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#ec-ground{{position:absolute;inset:0;background:linear-gradient(160deg,{YELLOW} 0%,#FFD21F 55%,#FFB21A 100%);}}
#ec-grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(10,15,44,0.07) 2px,transparent 2px),linear-gradient(90deg,rgba(10,15,44,0.07) 2px,transparent 2px);background-size:60px 60px;}}
#ec-syms{{position:absolute;inset:0;}}
.es{{position:absolute;font-weight:800;color:rgba(10,15,44,0.08);line-height:1;}}
#ec-q{{position:absolute;left:100px;top:400px;font-size:104px;font-weight:800;line-height:1.08;letter-spacing:-0.03em;color:{NAVY};}}
#ec-q .w{{display:inline-block;}}
#ec-cta{{position:absolute;left:100px;top:680px;font-size:50px;font-weight:700;color:{YELLOW};background:{NAVY};padding:14px 34px;border-radius:60px;box-shadow:0 20px 50px rgba(10,15,44,0.3);}}
#ec-logo{{position:absolute;left:100px;top:880px;width:320px;}}
#ec-handle{{position:absolute;left:100px;top:1220px;font-size:46px;font-weight:700;color:{NAVY};}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="ec-ground"></div>
    <div id="ec-grid"></div>
    <div id="ec-syms" data-layout-ignore>{sym_html}</div>
    <div id="ec-q">{words(l1)}<br>{words(l2)}</div>
    <div id="ec-cta">{esc(spec["cta"])}</div>
    <img id="ec-logo" src="assets/brand/sj-academy-logo-stacked-on-yellow.svg" alt="SJ Academy">
    <div id="ec-handle">{esc(spec["handle"])}</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#ec-ground,#ec-grid',{{clipPath:'circle(0% at 50% 50%)'}},{{clipPath:'circle(80% at 50% 50%)',duration:0.55,ease:'expo.inOut'}},0);
    tl.fromTo('#ec-syms',{{opacity:0,y:60}},{{opacity:1,y:-40,duration:{D},ease:'none'}},0.2);
    tl.fromTo('#ec-q .w',{{opacity:0,y:60,rotation:4}},{{opacity:1,y:0,rotation:0,duration:0.45,ease:'back.out(1.8)',stagger:0.08}},{t_v});
    tl.fromTo('#ec-cta',{{opacity:0,scale:0.4,rotation:-8}},{{opacity:1,scale:1,rotation:-2,duration:0.5,ease:'back.out(2)'}},{t_v + 1.1:.3f});
    tl.fromTo('#ec-logo',{{opacity:0,scale:1.3,rotation:-6,transformOrigin:'0% 50%'}},{{opacity:1,scale:1,rotation:0,duration:0.18,ease:'back.out(1.7)'}},{t_logo});
    tl.fromTo('#ec-handle',{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.35,ease:'power3.out'}},{t_logo + 0.35:.3f});
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, D, html_, [(spec["voice"], t_v)], [("fx-whoosh", 0.0), ("sj-sonic-logo-full", t_logo + 0.033)], t_logo

# ---------------------------------------------------------------- background: gradient, accent glows, chalk maths
def bg_scene(D, hits):
    cid = "bg"
    # v3 (26 Oct): calmer. A few faint notes kept to the top and bottom margins, two quiet line drawings,
    # no floating operators. Content sits on a clean field.
    chalk = [  # (text, x, y, size, rotation): Caveat, handwritten on a board
        ("a² + b² = c²", 640, 110, 60, -4), ("π ≈ 3.14159", 110, 1700, 58, 3),
        ("y = mx + c", 700, 1810, 58, -3), ("sin²θ + cos²θ = 1", 300, 1930, 54, 2),
    ]
    chalk_html = "".join(f'<div class="ck" style="left:{x}px;top:{y}px;font-size:{s}px;transform:rotate({r}deg)">{esc(t)}</div>'
                         for t, x, y, s, r in chalk)
    # line drawings in currentColor so they take the hack's accent
    par = " ".join(f"{'M' if i == 0 else 'L'}{740 + i * 6:.0f} {1960 - ((i * 6 - 150) ** 2) / 110:.0f}" for i in range(51))
    svg = f"""<svg id="bg-graphs" width="{W}" height="{H_ + 200}" viewBox="0 0 {W} {H_ + 200}">
  <g fill="none" stroke="currentColor" stroke-linecap="round">
    <path d="{par}" stroke-width="4"/>
    <circle cx="40" cy="40" r="170" stroke-width="3"/>
    <path d="M40 40 L187 -45 M40 40 L210 40" stroke-width="3"/>
  </g>
</svg>"""
    js = [f"tl.fromTo('#bg-chalk',{{y:0}},{{y:-140,duration:{D:.3f},ease:'none'}},0);",
          f"tl.fromTo('#bg-graphs',{{y:0}},{{y:-90,duration:{D:.3f},ease:'none'}},0);",
          f"tl.fromTo('#bg-g1',{{x:0,y:0}},{{x:160,y:260,duration:{D / 2:.3f},ease:'sine.inOut'}},0);",
          f"tl.to('#bg-g1',{{x:-60,y:120,duration:{D / 2:.3f},ease:'sine.inOut'}},{D / 2:.3f});",
          f"tl.fromTo('#bg-g2',{{x:0,y:0}},{{x:-160,y:-200,duration:{D / 2:.3f},ease:'sine.inOut'}},0);",
          f"tl.to('#bg-g2',{{x:40,y:-60,duration:{D / 2:.3f},ease:'sine.inOut'}},{D / 2:.3f});"]
    # every hit (hidden under its panel) moves the glows and graphs to that hack's accent
    for col, t in hits:
        js.append(f"tl.to('#bg-g1,#bg-graphs',{{color:'{col}',duration:0.35,ease:'none'}},{t + 0.15:.3f});")
        js.append(f"tl.to('#bg-g2',{{color:'{col}',duration:0.35,ease:'none'}},{t + 0.15:.3f});")
    html_ = f"""<template>
  <style>
{fonts()}
#root{{position:absolute;inset:0;overflow:hidden;font-family:'SJ Poppins';}}
#bg-base{{position:absolute;inset:0;background:radial-gradient(120% 80% at 20% 10%,{NAVY2} 0%,{NAVY} 60%,#05081C 100%);}}
#bg-g1{{position:absolute;left:-300px;top:-200px;width:1100px;height:1100px;border-radius:50%;color:{ACC[2]};
  background:radial-gradient(circle,currentColor 0%,transparent 68%);opacity:0.18;}}
#bg-g2{{position:absolute;left:400px;top:1100px;width:1100px;height:1100px;border-radius:50%;color:{ORANGE};
  background:radial-gradient(circle,currentColor 0%,transparent 68%);opacity:0.10;}}
#bg-grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,0.022) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,0.022) 2px,transparent 2px);
  background-size:60px 60px;-webkit-mask-image:radial-gradient(circle at 50% 45%,#000 20%,transparent 75%);mask-image:radial-gradient(circle at 50% 45%,#000 20%,transparent 75%);}}
#bg-graphs{{position:absolute;left:0;top:0;color:{ACC[2]};opacity:0.09;}}
#bg-chalk{{position:absolute;left:0;top:0;width:{W}px;height:{H_ + 200}px;}}
.ck{{position:absolute;white-space:nowrap;font-family:'SJ Caveat';font-weight:600;color:rgba(255,255,255,0.06);}}
#bg-vig{{position:absolute;inset:0;background:radial-gradient(130% 90% at 50% 45%,transparent 55%,rgba(3,5,18,0.75) 100%);}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}" data-layout-ignore>
    <div id="bg-base"></div>
    <div id="bg-g1"></div>
    <div id="bg-g2"></div>
    <div id="bg-grid"></div>
    {svg}
    <div id="bg-chalk">{chalk_html}</div>
    <div id="bg-vig"></div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join("    " + j for j in js)}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, html_

# ---------------------------------------------------------------- full-screen hits between hacks
def hits_scene(hits, D):
    """hits: (t, colour, big, small, dark_text). Panel sweeps in, number slams, number flies to the counter."""
    cid = "hits"
    body, js = [], []
    for j, (t, col, big, small, dark) in enumerate(hits):
        p = f"ht{j}"
        ink = NAVY if dark else "#FFFFFF"
        num_cls = "hn" if big.isdigit() else "hn hw"
        body.append(f'<div class="hp" id="{p}-panel" style="background:linear-gradient(135deg,{col} 0%,{shade(col, 0.72)} 60%,{shade(col, 0.45)} 100%)">'
                    f'<div class="hlines">{"".join(f"<i style=\"transform:rotate({a}deg)\"></i>" for a in range(0, 360, 30))}</div></div>')
        body.append(f'<div class="hx" id="{p}-x"><div class="{num_cls}" id="{p}-n" style="color:{ink}">{esc(big)}</div>'
                    f'<div class="hs" id="{p}-s" style="color:{ink}">{esc(small)}</div></div>')
        closed = "polygon(0% 0%, 0% 0%, -40% 100%, -40% 100%)"
        full = "polygon(0% 0%, 140% 0%, 100% 100%, -40% 100%)"
        gone = "polygon(140% 0%, 140% 0%, 100% 100%, 100% 100%)"
        js += [
            f"tl.set('#{p}-panel',{{clipPath:'{closed}'}},0);",
            f"tl.set('#{p}-x',{{opacity:0}},0);",
            f"tl.fromTo('#{p}-panel',{{clipPath:'{closed}'}},{{clipPath:'{full}',duration:0.24,ease:'power3.in'}},{t:.3f});",
            f"tl.fromTo('#{p}-panel .hlines',{{scale:0.4,rotation:0,opacity:0}},{{scale:1.3,rotation:20,opacity:1,duration:0.6,ease:'expo.out'}},{t + 0.2:.3f});",
            f"tl.fromTo('#{p}-x',{{opacity:0,scale:3,filter:'blur(24px)'}},{{opacity:1,scale:1,filter:'blur(0px)',duration:0.2,ease:'expo.out'}},{t + 0.12:.3f});",
            f"tl.fromTo('#{p}-x',{{x:-16,y:10}},{{x:0,y:0,duration:0.2,ease:'steps(5)'}},{t + 0.32:.3f});",
            f"tl.fromTo('#{p}-s',{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.2,ease:'power3.out'}},{t + 0.3:.3f});",
            f"tl.to('#{p}-panel',{{clipPath:'{gone}',duration:0.28,ease:'power3.inOut'}},{t + 0.62:.3f});",
        ]
        if big.isdigit():  # fly into the counter (top left)
            js.append(f"tl.to('#{p}-x',{{x:-300,y:-245,scale:0.36,opacity:0,duration:0.32,ease:'power3.in'}},{t + 0.6:.3f});")
        else:
            js.append(f"tl.to('#{p}-x',{{scale:1.6,opacity:0,filter:'blur(16px)',duration:0.3,ease:'power3.in'}},{t + 0.6:.3f});")
    html_ = f"""<template>
  <style>
{fonts()}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';overflow:hidden;}}
.hp{{position:absolute;inset:0;overflow:hidden;}}
.hlines{{position:absolute;left:540px;top:900px;width:0;height:0;}}
.hlines i{{position:absolute;left:0;top:-3px;width:1400px;height:6px;transform-origin:0 50%;
  background:linear-gradient(90deg,rgba(255,255,255,0.0) 10%,rgba(255,255,255,0.28) 30%,rgba(255,255,255,0) 70%);}}
.hx{{position:absolute;left:0;top:560px;width:{W}px;height:700px;text-align:center;transform-origin:50% 50%;}}
.hn{{font-size:480px;font-weight:800;line-height:1;letter-spacing:-0.05em;text-shadow:0 30px 80px rgba(5,8,28,0.35);}}
.hn.hw{{font-size:150px;padding-top:150px;letter-spacing:-0.03em;}}
.hs{{font-size:64px;font-weight:700;margin-top:10px;white-space:nowrap;}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}" data-layout-ignore>
    {chr(10).join("    " + b_ for b_ in body).strip()}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join("    " + j for j in js).strip()}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, html_

# ---------------------------------------------------------------- chrome: logo, counter and progress rail
def chrome_scene(rolls, fills):
    cid = "chrome"
    units = "".join(f'<div class="gold">{d}</div>' for d in list(range(10)) + [0])
    rail = "".join(f'<div class="seg"><i id="ch-s{j}" style="background:linear-gradient(90deg,{YELLOW},{ACC[j]})"></i></div>' for j in range(10))
    js = []
    for k, t in enumerate(rolls, 1):
        if k > 1:
            js.append(f"tl.fromTo('#ch-u',{{y:{-(k - 1) * COUNT_PX}}},{{y:{-k * COUNT_PX},duration:0.3,ease:'power3.inOut'}},{t:.3f});")
        if k == 10:
            js.append(f"tl.fromTo('#ch-t',{{y:0}},{{y:-{COUNT_PX},duration:0.3,ease:'power3.inOut'}},{t:.3f});")
    for k, t in enumerate(fills):
        js.append(f"tl.fromTo('#ch-s{k}',{{scaleX:0}},{{scaleX:1,duration:0.4,ease:'expo.out'}},{t:.3f});")
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#ch-logo{{position:absolute;left:100px;top:{LOGO_TOP}px;width:{LOGO_W}px;}}
#ch-count{{position:absolute;left:88px;top:{COUNT_TOP}px;font-size:{COUNT_PX}px;font-weight:800;line-height:1;letter-spacing:-0.05em;
  display:flex;align-items:flex-start;height:{COUNT_PX}px;overflow:hidden;filter:drop-shadow(0 16px 40px rgba(252,180,4,0.3));}}
.col{{display:flex;flex-direction:column;}}
.col div{{height:{COUNT_PX}px;text-align:center;}}
#ch-t{{margin-right:-6px;}}
#ch-of{{position:absolute;left:474px;top:{COUNT_TOP + 22}px;font-size:32px;font-weight:700;letter-spacing:0.2em;color:rgba(247,246,255,0.5);}}
#ch-rail{{position:absolute;right:100px;top:{LOGO_TOP + 22}px;display:flex;gap:8px;}}
.seg{{width:30px;height:10px;border-radius:5px;background:rgba(255,255,255,0.14);overflow:hidden;}}
.seg i{{display:block;width:100%;height:100%;transform-origin:0% 50%;transform:scaleX(0);}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <img id="ch-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
    <div id="ch-count" data-layout-ignore><div class="col" id="ch-t"><div class="gold">0</div><div class="gold">1</div></div><div class="col" id="ch-u">{units}</div></div>
    <div id="ch-of">HACK / 10</div>
    <div id="ch-rail">{rail}</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.set('#ch-u',{{y:-{COUNT_PX}}},0);
    {chr(10).join("    " + j for j in js).strip()}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, html_

# ---------------------------------------------------------------- captions
def chunks(s, maxw=760, size=40):
    import math
    words_ = s.split(" ")
    n = max(1, math.ceil(tw(s, size, 600) / maxw))
    while True:
        target = tw(s, size, 600) / n
        out, cur = [], ""
        for w in words_:
            nxt = (cur + " " + w).strip()
            if cur and tw(nxt, size, 600) > target * 1.08 and len(out) < n - 1:
                out.append(cur)
                cur = w
            else:
                cur = nxt
        out.append(cur)
        if all(tw(c, size, 600) <= maxw for c in out):
            return out
        n += 1

def caption_scene(placed, V):
    cid = "captions"
    groups, js = [], []
    n = 0
    for clip, t0 in placed:
        cs = chunks(V[clip]["text"])
        total = sum(len(c) for c in cs)
        t = t0
        for j, c in enumerate(cs):
            d = V[clip]["dur"] * len(c) / total
            end = t + d + (0.25 if j == len(cs) - 1 else 0)
            gid = f"cap{n}"
            groups.append(f'<div id="{gid}" class="clip cap" data-start="{t:.3f}" data-duration="{end - t:.3f}" data-track-index="1"><span id="{gid}-t">{esc(c)}</span></div>')
            js.append(f"tl.fromTo('#{gid}-t',{{opacity:0,y:16,scale:0.96}},{{opacity:1,y:0,scale:1,duration:0.16,ease:'power3.out'}},{t:.3f});")
            t += d
            n += 1
    html_ = f"""<template>
  <style>
{fonts()}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
.cap{{position:absolute;left:100px;right:100px;bottom:{CAP_BOTTOM}px;text-align:center;}}
.cap span{{display:inline-block;font-size:40px;font-weight:600;line-height:1.3;color:#FFFFFF;background:rgba(6,9,30,0.82);
  border:2px solid rgba(255,255,255,0.12);padding:12px 26px;border-radius:22px;box-shadow:0 14px 40px rgba(0,0,0,0.35);}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    {chr(10).join("    " + g for g in groups).strip()}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join("    " + j for j in js).strip()}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, html_

# ---------------------------------------------------------------- assemble
def build():
    import episode as E
    V = voice_lines()
    os.makedirs(os.path.join(HERE, "compositions"), exist_ok=True)
    scenes, voice_at, sfx_at = [], [], []
    hits = []   # (t, colour, big, small, dark_text)
    T = 0.0

    def add(cid, D, h, vo, fx):
        scenes.append((cid, T, D, h))
        voice_at.extend((c, T + t) for c, t in vo)
        sfx_at.extend((f, T + t) for f, t in fx)

    cid, D, h, vo, fx = intro_scene(E.INTRO, V)
    add(cid, D, h, vo, fx)
    T += D
    hack_starts = []
    for k, hk in enumerate(E.HACKS, 1):
        hits.append((T, ACC[k - 1], f"{k:02d}", hk["title"], True))
        T += HIT
        cid, D, h, vo, fx, _ = hack_scene(k, hk, V, (f"h{k}a", f"h{k}b"))
        hack_starts.append(T)
        add(cid, D, h, vo, fx)
        T += D
    hacks_end = T
    hits.append((T, YELLOW, "Cheat sheet", "save it for your test", True))
    T += HIT
    cid, D, h, vo, fx = recap_scene(E.RECAP, V)
    recap_start = T
    add(cid, D, h, vo, fx)
    T += D
    cid, D, h, vo, fx, t_logo = end_scene(E.END, V)
    end_start = T
    add(cid, D, h, vo, fx)
    T += D
    total = round(T, 3)
    logo_land = end_start + t_logo

    for t, *_ in hits:
        sfx_at += [("fx-whoosh", t - 0.05), ("fx-impact", t + 0.28)]

    for cid, s, d, h in scenes:
        open(os.path.join(HERE, f"compositions/{cid}.html"), "w").write(h)
    ch_start = hits[0][0] + 0.3          # appears while hit 01 covers the screen
    rolls = [t + 0.3 - ch_start for t, *_ in hits[:10]]
    fills = [s + 0.1 - ch_start for s in hack_starts]
    open(os.path.join(HERE, "compositions/chrome.html"), "w").write(chrome_scene(rolls, fills)[1])
    open(os.path.join(HERE, "compositions/captions.html"), "w").write(caption_scene(voice_at, V)[1])
    open(os.path.join(HERE, "compositions/hits.html"), "w").write(hits_scene(hits, total)[1])
    open(os.path.join(HERE, "compositions/bg.html"), "w").write(
        bg_scene(total, [(c, t) for t, c, *_ in hits[:10]] + [(ACC[2], hits[10][0])])[1])

    def host(cid, s, d, z, track, kind="graphics"):
        return (f'<div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s:.3f}" '
                f'data-duration="{d:.3f}" data-track-index="{track}" data-track-kind="{kind}" data-width="{W}" data-height="{H_}" style="z-index:{z}"></div>')
    hosts = [host("bg", 0, total, 1, 0)]
    for z, (cid, s, d, h) in enumerate(scenes, 2):
        hosts.append(host(cid, s, d, z, 2))
    hosts.append(host("chrome", ch_start, hacks_end - ch_start, 20, 3))
    hosts.append(host("captions", 0, total, 40, 5, "captions"))
    hosts.append(host("hits", 0, total, 60, 6))

    audio = []
    for c, t in voice_at:
        audio.append(f'<audio id="vo-{c}" class="clip" src="voice/{c}.wav" data-start="{t:.3f}" data-duration="{V[c]['dur']:.3f}" data-volume="1" data-track-index="10"></audio>')
    lanes, seen, fdur = [], [], {}
    for f, t in sorted(sfx_at, key=lambda x: x[1]):
        if any(f == f2 and abs(t - t2) < 0.15 for f2, t2 in seen):
            continue
        seen.append((f, t))
        d = fdur.setdefault(f, dur(os.path.join(HERE, f"assets/sfx/{f}.wav")))
        lane = next((i for i, e in enumerate(lanes) if e <= t), None)
        if lane is None:
            lanes.append(0)
            lane = len(lanes) - 1
        lanes[lane] = t + d + 0.01
        vol = {"sj-sonic-logo-full": 0.5, "fx-impact": 0.42, "fx-whoosh": 0.36, "fx-pop": 0.22}.get(f, 0.32)
        audio.append(f'<audio id="fx{len(seen)}" class="clip" src="assets/sfx/{f}.wav" data-start="{max(t, 0):.3f}" data-duration="{d:.3f}" data-volume="{vol}" data-track-index="{11 + lane}"></audio>')
    mus_end = logo_land - 0.1
    audio.append(f'<audio id="music" class="clip" src="assets/music/lofi.mp3" data-start="0" data-duration="{mus_end:.3f}" data-volume="0.13" data-fade-in="0.2" data-fade-out="1.6" data-track-index="9"></audio>')

    index = f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H_}" />
    <!-- Generated by build.py from episode.py. Edit those, then run python3 build.py -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: {W}px; height: {H_}px; overflow: hidden; background: {NAVY}; }}
      #root {{ width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total:.3f}" data-width="{W}" data-height="{H_}">
      {chr(10).join("      " + x for x in hosts).strip()}
      {chr(10).join("      " + x for x in audio).strip()}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
    open(os.path.join(HERE, "index.html"), "w").write(index)
    timing = dict(total=total, hits=[round(h[0], 3) for h in hits], hack_starts=[round(x, 3) for x in hack_starts],
                  recap=round(recap_start, 3), end=round(end_start, 3), voice={c: round(t, 3) for c, t in voice_at})
    json.dump(timing, open(os.path.join(HERE, "timing.json"), "w"), indent=1)
    print(f"built {len(scenes)} scenes, {total:.1f}s")

if __name__ == "__main__":
    build()
