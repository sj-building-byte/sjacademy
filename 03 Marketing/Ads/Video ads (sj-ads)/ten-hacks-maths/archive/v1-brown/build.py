# Builds the "10 Hacks" video from episode.py and the voice clips in voice/.
# Writes index.html, compositions/*.html and timing.json. Run: python3 build.py
# Layout, colours and motion follow SPEC.md. Voice: ./make-voice.sh first.
import json, os, re, subprocess, html

HERE = os.path.dirname(os.path.abspath(__file__))
W, H_ = 1080, 1920
BROWN, YELLOW, ORANGE, CREAM = "#453516", "#FCE004", "#FE6100", "#FFF6DC"
METRICS = json.load(open(os.path.join(HERE, "assets/brand/poppins-metrics.json")))
X0 = 90

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
#root{{position:absolute;inset:0;font-family:'SJ Poppins';color:{CREAM};font-kerning:none;}}
.tk{{position:absolute;white-space:pre;line-height:1.2;z-index:2;}}
.note{{position:absolute;white-space:pre;font-family:'SJ Caveat';font-weight:600;color:{ORANGE};line-height:1.2;z-index:2;}}
.box{{position:absolute;background:{YELLOW};border-radius:10px;z-index:1;transform-origin:50% 50%;}}
.bar{{position:absolute;height:7px;border-radius:4px;background:{CREAM};z-index:2;}}
svg.pen{{position:absolute;left:0;top:0;overflow:visible;z-index:2;}}
"""

def esc(s):
    return html.escape(s, quote=True)

# ---------------------------------------------------------------- hack scene
def hack_scene(k, hk, V, clips):
    cid = f"h{k:02d}"
    P = cid + "-"
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
    state = {i: dict(op=0.0, col=CREAM if it.get("tone") != "dim" else "rgba(255,246,220,0.62)")
             for i, it in items.items()}

    # title and rule
    rule_html = "".join(
        f'<span class="{"hl" if h else ""}" id="{P}r{j}">{esc(s)}</span>' for j, (s, h) in enumerate(hk["rule"]))
    words = hk["title"].split(" ")
    title_html = " ".join(f'<span class="w" id="{P}tw{j}">{esc(w)}</span>' for j, w in enumerate(words))
    body.append(f'<div class="title" id="{P}title">{title_html}</div>')
    body.append(f'<div class="rule" id="{P}rule">{rule_html}</div>')
    js.append(f"tl.fromTo('#{P}title .w',{{opacity:0,filter:'blur(8px)'}},{{opacity:1,filter:'blur(0px)',duration:0.2,ease:'power4.out',stagger:0.07}},0.12);")
    js.append(f"tl.fromTo('#{P}rule',{{opacity:0,filter:'blur(8px)'}},{{opacity:1,filter:'blur(0px)',duration:0.22,ease:'power4.out'}},0.28);")

    for it in hk["items"]:
        i = P + it["id"]
        if it["kind"] == "t":
            col = state[it["id"]]["col"]
            body.append(f'<div class="tk" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - it["size"] * 0.6:.1f}px;'
                        f'font-size:{it["size"]}px;font-weight:{it["weight"]};color:{col}">{esc(it["s"])}</div>')
        elif it["kind"] == "note":
            body.append(f'<div class="note" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - it["size"] * 0.62:.1f}px;'
                        f'font-size:{it["size"]}px">{esc(it["s"])}</div>')
        elif it["kind"] == "bar":
            body.append(f'<div class="bar" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - 3:.1f}px;width:{it["w"]:.1f}px"></div>')
        elif it["kind"] == "arrow":
            body.append(f'<svg class="pen" id="{i}" style="left:{it["x"]:.1f}px;top:{it["y"] - 30:.1f}px" width="{it["w"]:.0f}" height="60">'
                        f'<path id="{i}-p" d="{it["d"]}" fill="none" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
        elif it["kind"] == "path":
            body.append(f'<svg class="pen" id="{i}" width="{W}" height="{H_}"><path id="{i}-p" d="{it["d"]}" fill="none" '
                        f'stroke="{CREAM}" stroke-width="{it["width"]}" stroke-linecap="round" stroke-linejoin="round"/></svg>')
        js.append(f"tl.set('#{i}',{{opacity:0}},0);")
        if it["kind"] in ("arrow", "path"):
            js.append(f"tl.set('#{i}-p',{{strokeDasharray:{it['length']},strokeDashoffset:{it['length']}}},0);")

    def sel(ids):
        return ",".join("#" + P + x for x in ids)

    def fade(ids, t, to, dur_=0.2, blur=True):
        for x in ids:
            fr = state[x]["op"]
            f0 = ",filter:'blur(8px)'" if blur and to > fr else ""
            f1 = ",filter:'blur(0px)'" if blur and to > fr else ""
            js.append(f"tl.fromTo('#{P}{x}',{{opacity:{fr}{f0}}},{{opacity:{to}{f1},duration:{dur_},ease:'power4.out'}},{t});")
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
        elif act == "dim":
            fade(ev[2], t, 0.32, 0.3, blur=False)
        elif act == "out":
            for x in ev[2]:
                js.append(f"tl.fromTo('#{P}{x}',{{opacity:{state[x]['op']},filter:'blur(0px)'}},{{opacity:0,filter:'blur(6px)',duration:0.18,ease:'expo.in'}},{t});")
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
                lift = -70 if act == "swap" and dx < 0 else (70 if act == "swap" else 0)
                js.append(f"tl.set('#{P}{dst}',{{opacity:1,transformOrigin:'0% 50%'}},{t});")
                js.append(f"tl.fromTo('#{P}{dst}',{{x:{dx:.1f},scale:{sc:.3f}}},{{x:0,scale:1,duration:0.62,ease:'power3.inOut'}},{t});")
                if lift:
                    js.append(f"tl.fromTo('#{P}{dst}',{{y:{dy:.1f}}},{{y:{lift},duration:0.31,ease:'power2.out'}},{t});")
                    js.append(f"tl.to('#{P}{dst}',{{y:0,duration:0.31,ease:'power2.in'}},{t + 0.31:.3f});")
                else:
                    js.append(f"tl.fromTo('#{P}{dst}',{{y:{dy:.1f}}},{{y:0,duration:0.62,ease:'power2.inOut'}},{t});")
                state[dst]["op"] = 1
            sfx.append(("fx-pop", t + 0.55))
        elif act == "drop":
            x = ev[2]
            js.append(f"tl.fromTo('#{P}{x}',{{opacity:0,y:-90,scale:1.25}},{{opacity:1,y:0,scale:1,duration:0.3,ease:'back.out(1.7)'}},{t});")
            state[x]["op"] = 1
            sfx.append(("fx-pop", t + 0.2))
        elif act == "note":
            x = ev[2]
            js.append(f"tl.fromTo('#{P}{x}',{{opacity:1,clipPath:'inset(0% 100% 0% 0%)'}},{{clipPath:'inset(0% 0% 0% 0%)',duration:0.4,ease:'sine.inOut'}},{t});")
            state[x]["op"] = 1
        elif act == "draw":
            x = ev[2]
            ln = items[x]["length"]
            js.append(f"tl.set('#{P}{x}',{{opacity:1}},{t});")
            js.append(f"tl.fromTo('#{P}{x}-p',{{strokeDashoffset:{ln}}},{{strokeDashoffset:0,duration:{0.33 if items[x]['kind'] == 'arrow' else 0.6},ease:'sine.inOut'}},{t});")
            state[x]["op"] = 1
        elif act == "hl_rule":
            hl_rule_t = t
            js.append(f"tl.fromTo('#{P}rule .hl',{{backgroundSize:'0% 100%',color:'{CREAM}'}},{{backgroundSize:'100% 100%',color:'{BROWN}',duration:0.3,ease:'power2.out'}},{t});")
            sfx.append(("sj-sfx-highlighter-swipe", t))
        elif act == "stamp":
            ids = ev[2]
            its = [items[x] for x in ids]
            x0 = min(i_["x"] for i_ in its) - 18
            x1 = max(i_["x1"] for i_ in its) + 18
            y0 = min(i_["y"] - i_["size"] * 0.62 for i_ in its) - 2
            y1 = max(i_["y"] + i_["size"] * 0.55 for i_ in its) + 2
            bid = f"{P}box{nbox}"
            nbox += 1
            body.append(f'<div class="box" id="{bid}" style="left:{x0:.1f}px;top:{y0:.1f}px;width:{x1 - x0:.1f}px;height:{y1 - y0:.1f}px"></div>')
            js.append(f"tl.set('#{bid}',{{opacity:0}},0);")
            js.append(f"tl.fromTo('#{bid}',{{opacity:0,scale:1.3,rotation:-7}},{{opacity:1,scale:1,rotation:-1.5,duration:0.14,ease:'back.out(1.7)'}},{t});")
            js.append(f"tl.fromTo('#{bid}',{{x:2}},{{x:0,duration:0.13,ease:'steps(4)'}},{t + 0.14:.3f});")
            for x in ids:
                if items[x]["kind"] == "bar":
                    js.append(f"tl.fromTo('#{P}{x}',{{backgroundColor:'{CREAM}'}},{{backgroundColor:'{BROWN}',duration:0.05}},{t + 0.04:.3f});")
                else:
                    if state[x]["op"] < 1:
                        js.append(f"tl.fromTo('#{P}{x}',{{opacity:{state[x]['op']}}},{{opacity:1,duration:0.08}},{t});")
                        state[x]["op"] = 1
                    js.append(f"tl.fromTo('#{P}{x}',{{color:'{state[x]['col']}'}},{{color:'{BROWN}',duration:0.05}},{t + 0.04:.3f});")
                    state[x]["col"] = BROWN
            sfx.append(("sj-sfx-stamp", t + 0.03))
        else:
            raise SystemExit(f"{cid}: unknown action {act}")

    never = [i for i in items if i not in shown]
    if never:
        raise SystemExit(f"{cid}: never appears: {never}")
    # exit: the whole board blurs out; even scenes leave upward
    up = ",y:-60" if k % 2 == 0 else ""
    js.append(f"tl.fromTo('#{P}stage',{{opacity:1,filter:'blur(0px)',y:0}},{{opacity:0,filter:'blur(10px)'{up},duration:0.22,ease:'expo.in'}},{D - 0.24:.3f});")

    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#{P}stage{{position:absolute;inset:0;}}
#{P}title{{position:absolute;left:390px;top:426px;width:600px;font-size:76px;font-weight:700;line-height:1.1;letter-spacing:-0.01em;}}
#{P}title .w{{display:inline-block;}}
#{P}rule{{position:absolute;left:{X0}px;top:590px;width:880px;font-size:42px;font-weight:500;line-height:1.38;color:rgba(255,246,220,0.86);}}
#{P}rule .hl{{background-image:linear-gradient({YELLOW},{YELLOW});background-repeat:no-repeat;background-size:0% 100%;
  padding:0 6px;border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone;font-weight:600;}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="{P}stage" data-layout-allow-overlap>
      {chr(10).join("      " + b_ for b_ in body).strip()}
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
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#in-big{{position:absolute;left:58px;top:330px;font-size:560px;font-weight:800;line-height:1;letter-spacing:-0.05em;color:{YELLOW};}}
#in-title{{position:absolute;left:{X0}px;top:880px;font-size:132px;font-weight:800;line-height:1;letter-spacing:-0.03em;white-space:nowrap;}}
#in-hl{{background-image:linear-gradient({YELLOW},{YELLOW});background-repeat:no-repeat;background-size:0% 100%;padding:0 14px;border-radius:12px;}}
#in-sub{{position:absolute;left:{X0}px;top:1050px;font-size:44px;font-weight:500;color:rgba(255,246,220,0.86);}}
#in-sub .w{{display:inline-block;}}
#in-tick{{position:absolute;left:0;top:300px;font-size:40px;font-weight:600;white-space:nowrap;color:rgba(255,246,220,0.34);}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="in-stage">
      <div id="in-tick" data-layout-allow-overflow data-layout-ignore>{tick}</div>
      <div id="in-big">{esc(spec["big"])}</div>
      <div id="in-title">{esc(t1)}<span id="in-hl">{esc(t2)}</span></div>
      <div id="in-sub">{" ".join(f'<span class="w">{esc(w)}</span>' for w in spec["sub"].split(" "))}</div>
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#in-tick',{{x:0}},{{x:-{tw(spec["ticker"], 40, 600):.0f},duration:{D},ease:'none'}},0);
    tl.fromTo('#in-big',{{scale:1.04,transformOrigin:'0% 50%'}},{{scale:1,duration:0.7,ease:'expo.out'}},0);
    tl.fromTo('#in-hl',{{backgroundSize:'0% 100%',color:'{CREAM}'}},{{backgroundSize:'100% 100%',color:'{BROWN}',duration:0.3,ease:'power2.out'}},0.35);
    tl.fromTo('#in-sub .w',{{opacity:0,filter:'blur(6px)'}},{{opacity:1,filter:'blur(0px)',duration:0.16,ease:'power4.out',stagger:0.08}},0.7);
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, D, html_, [(spec["voice"], t_v)], [("sj-sfx-highlighter-swipe", 0.35)]

def recap_scene(spec, V):
    cid = "recap"
    t_v = 0.45
    D = round(t_v + V[spec["voice"]]["dur"] + 1.7, 3)
    rows = []
    for j, r in enumerate(spec["rows"]):
        assert tw(f"{j + 1:02d}  " + r, 36, 500) < 880, r
        rows.append(f'<div class="rr" id="rc-r{j}"><span class="rn">{j + 1:02d}</span>{esc(r)}</div>')
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#rc-title{{position:absolute;left:{X0}px;top:330px;font-size:72px;font-weight:800;letter-spacing:-0.02em;}}
#rc-hl{{background-image:linear-gradient({YELLOW},{YELLOW});background-repeat:no-repeat;background-size:0% 100%;padding:0 10px;border-radius:10px;}}
#rc-list{{position:absolute;left:{X0}px;top:470px;width:900px;}}
.rr{{font-size:36px;font-weight:500;line-height:1;height:66px;display:flex;align-items:center;border-bottom:2px solid rgba(255,246,220,0.12);white-space:nowrap;}}
.rn{{display:inline-block;width:78px;font-weight:800;color:{YELLOW};}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="rc-title">Your <span id="rc-hl">cheat sheet</span></div>
    <div id="rc-list">
      {chr(10).join("      " + r for r in rows).strip()}
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#rc-title',{{opacity:0,filter:'blur(8px)'}},{{opacity:1,filter:'blur(0px)',duration:0.2,ease:'power4.out'}},0.05);
    tl.fromTo('.rr',{{opacity:0,x:-40}},{{opacity:1,x:0,duration:0.4,ease:'expo.out',stagger:0.06}},0.2);
    tl.fromTo('#rc-hl',{{backgroundSize:'0% 100%',color:'{CREAM}'}},{{backgroundSize:'100% 100%',color:'{BROWN}',duration:0.3,ease:'power2.out'}},0.95);
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
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#ec-ground{{position:absolute;inset:0;background:{YELLOW};}}
#ec-q{{position:absolute;left:{X0}px;top:400px;font-size:96px;font-weight:800;line-height:1.08;letter-spacing:-0.02em;color:{BROWN};}}
#ec-q .w{{display:inline-block;}}
#ec-cta{{position:absolute;left:{X0}px;top:650px;font-size:52px;font-weight:600;color:{BROWN};}}
#ec-cta span{{background:{BROWN};color:{YELLOW};padding:4px 22px;border-radius:12px;}}
#ec-logo{{position:absolute;left:{X0}px;top:860px;width:300px;}}
#ec-handle{{position:absolute;left:{X0}px;top:1180px;font-size:44px;font-weight:600;color:{BROWN};}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="ec-ground"></div>
    <div id="ec-q">{" ".join(f'<span class="w">{esc(w)}</span>' for w in l1.split(" "))}<br>{" ".join(f'<span class="w">{esc(w)}</span>' for w in l2.split(" "))}</div>
    <div id="ec-cta"><span>{esc(spec["cta"])}</span></div>
    <img id="ec-logo" src="assets/brand/sj-academy-logo-stacked-on-yellow.svg" alt="SJ Academy">
    <div id="ec-handle">{esc(spec["handle"])}</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#ec-ground',{{clipPath:'inset(100% 0% 0% 0%)'}},{{clipPath:'inset(0% 0% 0% 0%)',duration:0.42,ease:'power2.inOut'}},0);
    tl.fromTo('#ec-q .w',{{opacity:0,filter:'blur(8px)'}},{{opacity:1,filter:'blur(0px)',duration:0.18,ease:'power4.out',stagger:0.08}},{t_v});
    tl.fromTo('#ec-cta',{{opacity:0,x:-60,rotation:-4}},{{opacity:1,x:0,rotation:-1,duration:0.6,ease:'expo.out'}},{t_v + 1.1:.3f});
    tl.fromTo('#ec-logo',{{opacity:0,scale:1.3,rotation:-6,transformOrigin:'0% 50%'}},{{opacity:1,scale:1,rotation:0,duration:0.14,ease:'back.out(1.7)'}},{t_logo});
    tl.fromTo('#ec-handle',{{opacity:0,filter:'blur(6px)'}},{{opacity:1,filter:'blur(0px)',duration:0.25,ease:'power4.out'}},{t_logo + 0.35:.3f});
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, D, html_, [(spec["voice"], t_v)], [("sj-sfx-paper-slide", 0.0), ("sj-sonic-logo-full", t_logo + 0.033)], t_logo

# ---------------------------------------------------------------- chrome: counter and progress rail
def chrome_scene(starts, D):
    cid = "chrome"
    units = "".join(f"<div>{d}</div>" for d in list(range(10)) + [0])
    rail = "".join(f'<div class="seg"><i id="ch-s{j}"></i></div>' for j in range(10))
    js = []
    for k, t in enumerate(starts, 1):
        if k > 1:
            js.append(f"tl.fromTo('#ch-u',{{y:{-(k - 1) * 210}}},{{y:{-k * 210},duration:0.45,ease:'power3.inOut'}},{t - 0.1:.3f});")
        if k == 10:
            js.append(f"tl.fromTo('#ch-t',{{y:0}},{{y:-210,duration:0.45,ease:'power3.inOut'}},{t - 0.1:.3f});")
        js.append(f"tl.fromTo('#ch-s{k - 1}',{{scaleX:0}},{{scaleX:1,duration:0.25,ease:'power2.out'}},{t + 0.05:.3f});")
    html_ = f"""<template>
  <style>
{fonts()}
{BASE_CSS}
#ch-count{{position:absolute;left:78px;top:330px;font-size:210px;font-weight:800;line-height:1;letter-spacing:-0.04em;color:{YELLOW};display:flex;align-items:flex-start;height:210px;overflow:hidden;}}
.col{{display:flex;flex-direction:column;}}
.col div{{height:210px;text-align:right;}}
#ch-logo{{position:absolute;left:{X0}px;top:280px;width:200px;}}
#ch-of{{position:absolute;left:392px;top:372px;font-size:40px;font-weight:600;color:rgba(255,246,220,0.5);}}
#ch-rail{{position:absolute;right:90px;top:298px;display:flex;gap:8px;}}
.seg{{width:30px;height:10px;border-radius:5px;background:rgba(255,246,220,0.16);overflow:hidden;}}
.seg i{{display:block;width:100%;height:100%;background:{YELLOW};transform-origin:0% 50%;transform:scaleX(0);}}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H_}">
    <div id="ch-count" data-layout-ignore><div class="col" id="ch-t"><div>0</div><div>1</div></div><div class="col" id="ch-u">{units}</div></div>
    <img id="ch-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
    <div id="ch-of">/ 10</div>
    <div id="ch-rail">{rail}</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.set('#ch-u',{{y:-210}},0);
    {chr(10).join("    " + j for j in js).strip()}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
    return cid, html_

# ---------------------------------------------------------------- captions
def chunks(s, maxw=700, size=40):
    import math
    words = s.split(" ")
    n = max(1, math.ceil(tw(s, size, 500) / maxw))
    while True:
        target = tw(s, size, 500) / n
        out, cur = [], ""
        for w in words:
            nxt = (cur + " " + w).strip()
            if cur and tw(nxt, size, 500) > target * 1.08 and len(out) < n - 1:
                out.append(cur)
                cur = w
            else:
                cur = nxt
        out.append(cur)
        if all(tw(c, size, 500) <= maxw for c in out):
            return out
        n += 1

def _old_chunks(s, maxw=700, size=40):
    words, out, cur = s.split(" "), [], ""
    for w in words:
        nxt = (cur + " " + w).strip()
        if tw(nxt, size, 500) > maxw and cur:
            out.append(cur)
            cur = w
        else:
            cur = nxt
        if cur.endswith((",", ".", "?")) and tw(cur, size, 500) > maxw * 0.45:
            out.append(cur)
            cur = ""
    if cur:
        out.append(cur)
    return out

def caption_scene(placed, V, D):
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
            js.append(f"tl.fromTo('#{gid}-t',{{opacity:0}},{{opacity:1,duration:0.1}},{t:.3f});")
            t += d
            n += 1
    html_ = f"""<template>
  <style>
{fonts()}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
.cap{{position:absolute;left:{X0}px;bottom:{1920 - 1250}px;max-width:760px;}}
.cap span{{display:inline-block;font-size:40px;font-weight:500;line-height:1.3;color:{CREAM};background:rgba(30,22,8,0.78);padding:10px 20px;border-radius:12px;}}
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
    scenes, voice_at, sfx_at, timing = [], [], [], {}
    T = 0.0

    cid, D, h, vo, fx = intro_scene(E.INTRO, V)
    scenes.append((cid, T, D, h)); voice_at += [(c, T + t) for c, t in vo]; sfx_at += [(f, T + t) for f, t in fx]
    T += D
    hack_starts, rule_hl = [], []
    for k, hk in enumerate(E.HACKS, 1):
        cid, D, h, vo, fx, _ = hack_scene(k, hk, V, (f"h{k}a", f"h{k}b"))
        hack_starts.append(T)
        scenes.append((cid, T, D, h)); voice_at += [(c, T + t) for c, t in vo]; sfx_at += [(f, T + t) for f, t in fx]
        sfx_at.append(("sj-sfx-pen-tick", T + 0.08))
        T += D
    hacks_end = T
    cid, D, h, vo, fx = recap_scene(E.RECAP, V)
    recap_start = T
    scenes.append((cid, T, D, h)); voice_at += [(c, T + t) for c, t in vo]; sfx_at += [(f, T + t) for f, t in fx]
    T += D
    cid, D, h, vo, fx, t_logo = end_scene(E.END, V)
    end_start = T
    scenes.append((cid, T, D, h)); voice_at += [(c, T + t) for c, t in vo]; sfx_at += [(f, T + t) for f, t in fx]
    T += D
    total = round(T, 3)
    logo_land = end_start + t_logo

    for cid, s, d, h in scenes:
        open(os.path.join(HERE, f"compositions/{cid}.html"), "w").write(h)
    ccid, ch = chrome_scene([s - hack_starts[0] for s in hack_starts], hacks_end - hack_starts[0])
    open(os.path.join(HERE, "compositions/chrome.html"), "w").write(ch)
    capid, caph = caption_scene(voice_at, V, total)
    open(os.path.join(HERE, "compositions/captions.html"), "w").write(caph)

    hosts = []
    for z, (cid, s, d, h) in enumerate(scenes, 2):
        hosts.append(f'<div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s:.3f}" data-duration="{d:.3f}" data-track-index="2" data-track-kind="graphics" data-width="{W}" data-height="{H_}" style="z-index:{z}"></div>')
    hosts.append(f'<div id="chrome" data-composition-id="chrome" data-composition-src="compositions/chrome.html" data-start="{hack_starts[0]:.3f}" data-duration="{hacks_end - hack_starts[0]:.3f}" data-track-index="3" data-track-kind="graphics" data-width="{W}" data-height="{H_}" style="z-index:20"></div>')
    hosts.append(f'<div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{total:.3f}" data-track-index="5" data-track-kind="captions" data-width="{W}" data-height="{H_}" style="z-index:40"></div>')

    sfx_at.append(("sj-sfx-highlighter-swipe", hack_starts[0] - 0.3))
    sfx_at.append(("sj-sfx-highlighter-swipe", recap_start - 0.3))
    audio = []
    for j, (c, t) in enumerate(voice_at):
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
        vol = 0.5 if "sonic" in f else 0.32
        audio.append(f'<audio id="fx{len(seen)}" class="clip" src="assets/sfx/{f}.wav" data-start="{max(t, 0):.3f}" data-duration="{d:.3f}" data-volume="{vol}" data-track-index="{11 + lane}"></audio>')
    mus_end = logo_land - 0.1
    audio.append(f'<audio id="music" class="clip" src="assets/music/lofi.mp3" data-start="0" data-duration="{mus_end:.3f}" data-volume="0.13" data-fade-in="0.2" data-fade-out="1.6" data-track-index="9"></audio>')

    w1, w2 = hack_starts[0], recap_start
    index = f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H_}" />
    <!-- Generated by build.py from episode.py. Edit those, then run python3 build.py -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: {W}px; height: {H_}px; overflow: hidden; background: {BROWN}; }}
      #root {{ width: 100%; height: 100%; }}
      #ground {{ position: absolute; inset: 0; background-color: {BROWN};
        background-image: linear-gradient(rgba(255,246,220,0.05) 2px, transparent 2px), linear-gradient(90deg, rgba(255,246,220,0.05) 2px, transparent 2px);
        background-size: 60px 60px; background-position: -1px 9px; }}
      #logo {{ position: absolute; left: {X0}px; top: 280px; width: 200px; z-index: 30; }}
      .wipe {{ position: absolute; inset: 0; z-index: 60; }}
      .wipe i {{ position: absolute; inset: 0; background: {YELLOW}; display: block; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total:.3f}" data-width="{W}" data-height="{H_}">
      <div id="ground" class="clip" data-start="0" data-duration="{total:.3f}" data-track-index="0"></div>
      {chr(10).join("      " + x for x in hosts).strip()}
      <div id="wipe1" class="clip wipe" data-start="{w1 - 0.3:.3f}" data-duration="0.6" data-track-index="6"><i id="wipe1-b"></i></div>
      <div id="wipe2" class="clip wipe" data-start="{w2 - 0.3:.3f}" data-duration="0.6" data-track-index="6"><i id="wipe2-b"></i></div>
      {chr(10).join("      " + x for x in audio).strip()}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      [["#wipe1-b", {w1:.3f}], ["#wipe2-b", {w2:.3f}]].forEach(([s, t]) => {{
        tl.fromTo(s, {{ scaleX: 0, transformOrigin: "0% 50%" }}, {{ scaleX: 1, duration: 0.3, ease: "power2.in" }}, t - 0.3);
        tl.set(s, {{ transformOrigin: "100% 50%" }}, t);
        tl.fromTo(s, {{ scaleX: 1 }}, {{ scaleX: 0, duration: 0.29, ease: "power2.out", immediateRender: false }}, t);
      }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
    open(os.path.join(HERE, "index.html"), "w").write(index)
    timing = dict(total=total, hack_starts=[round(x, 3) for x in hack_starts], recap=round(recap_start, 3),
                  end=round(end_start, 3), voice={c: round(t, 3) for c, t in voice_at})
    json.dump(timing, open(os.path.join(HERE, "timing.json"), "w"), indent=1)
    print(f"built {len(scenes)} scenes, {total:.1f}s")

if __name__ == "__main__":
    build()
