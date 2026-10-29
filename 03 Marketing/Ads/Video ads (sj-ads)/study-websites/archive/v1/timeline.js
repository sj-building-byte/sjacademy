      // Root timeline. Times are seconds on the film's clock; voice line k runs L[k][0] to L[k][1].
      const tl = gsap.timeline({ paused: true });
      const { L, GO, STOP, END_CARD, DUR } = CFG;
      const IN = "expo.out", OUT = "expo.in", MOVE = "power2.inOut", POP = "back.out(1.7)";
      const s = (k) => L[k][0], e = (k) => L[k][1], d = (k) => L[k][1] - L[k][0];
      const at = (k, f) => s(k) + f * d(k);  // a point part-way through a voice line
      const fmt = (t) => { const m = Math.floor(t / 60), sec = t - m * 60; return `${m}:${sec.toFixed(2).padStart(5, "0")}`; };
      const shake = (sel, t) => tl.fromTo(sel, { x: 0 }, { keyframes: [{ x: -10 }, { x: 9 }, { x: -6 }, { x: 4 }, { x: 0 }], duration: 0.22, ease: "none" }, t);
      const slam = (sel, t, from = 1.6) => tl.fromTo(sel, { opacity: 0, scale: from, rotation: -4 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.28, ease: "expo.out" }, t);
      const pop = (sel, t) => tl.fromTo(sel, { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.4, ease: POP }, t);
      const sticker = (sel, t) => tl.fromTo(sel, { opacity: 0, scale: 1.4, rotation: -12 }, { opacity: 1, scale: 1, rotation: -4, duration: 0.3, ease: POP }, t);

      // ---------- the stopwatch: runs from "Let's go!" to "Time!"
      const clock = { t: 0 };
      const timerEl = document.getElementById("timer");
      tl.fromTo(clock, { t: 0 }, { t: STOP - GO, duration: STOP - GO, ease: "none", onUpdate: () => { timerEl.textContent = fmt(clock.t); } }, GO);
      tl.fromTo("#timer", { scale: 1.18 }, { scale: 1, duration: 0.4, ease: IN }, GO);

      // ---------- splits: each row names its site when it starts, and stamps its time when it's done
      CFG.TOOLS.forEach((tid, i) => {
        const [a] = CFG.SEG[tid], done = CFG.DONE[i];
        const st = document.getElementById(`st${i}`);
        st.innerHTML = `<span class="d0">–</span><span class="d1" style="display:none">${fmt(done - GO)}</span>`;
        tl.set(`#sr${i} .nm`, { display: "none" }, a);
        tl.set(`#sr${i} .real`, { display: "inline" }, a);
        tl.to(`#sr${i}`, { color: "#ffffff", duration: 0.2, ease: "none" }, a);
        tl.to(`#pip${i}`, { backgroundColor: "rgba(252,224,4,0.4)", duration: 0.2, ease: "none" }, a);
        tl.set(`#st${i} .d0`, { display: "none" }, done);
        tl.set(`#st${i} .d1`, { display: "inline" }, done);
        tl.fromTo(`#st${i}`, { color: "#151515", backgroundColor: "#FCE004", scale: 1.3 }, { color: "#FCE004", backgroundColor: "rgba(252,224,4,0)", scale: 1, duration: 0.6, ease: IN, immediateRender: false }, done);
        tl.to(`#pip${i}`, { backgroundColor: "#FCE004", duration: 0.15, ease: "none" }, done);
      });

      // ---------- the hook: four slams, then GO!
      slam("#hk1", at("01", 0.0));
      slam("#hk2", at("01", 0.3));
      slam("#hk3", at("01", 0.62));
      tl.fromTo("#go", { opacity: 0, scale: 2.4, rotation: -14 }, { opacity: 1, scale: 1, rotation: -6, duration: 0.18, ease: "power4.in" }, GO - 0.32);
      shake("#go", GO - 0.14);
      tl.to("#hk1, #hk2, #hk3, #go", { opacity: 0, y: -60, duration: 0.3, ease: OUT, stagger: 0.03 }, GO + 0.25);

      // ---------- every site: the question slides in, the browser window rises, both whip out at the end
      CFG.TOOLS.forEach((tid) => {
        const [a, b] = CFG.SEG[tid];
        tl.fromTo(`#qh-${tid}`, { opacity: 0, x: 140 }, { opacity: 1, x: 0, duration: 0.5, ease: IN }, a);
        tl.fromTo(`#win-${tid}`, { opacity: 0, y: 90, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: IN }, a + 0.08);
        tl.to([`#qh-${tid}`, `#win-${tid}`], { opacity: 0, x: -160, duration: 0.25, ease: OUT }, b - 0.27);
      });

      // 1 Desmos: type the two equations, then ping both crossings
      tl.fromTo("#d-eq", { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.9, ease: "none" }, s("03") + 0.1);
      tl.fromTo("#img-desmos", { opacity: 0.25 }, { opacity: 1, duration: 0.4, ease: "none" }, s("03") + 1.1);
      pop("#ping1", s("04") + 0.05);
      pop("#ping2", s("04") + 0.75);
      tl.to("#img-desmos", { scale: 1.08, transformOrigin: "60% 50%", duration: 0.8, ease: MOVE }, s("04"));
      pop("#d-ans", s("04") + 1.3);
      sticker("#d-note", s("05") + 0.4);

      // 2 PhET: the resistance slider goes up, the current halves
      pop("#p-ring", s("06") + 1.4);
      tl.fromTo("#img-p1", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "none" }, s("07") + 0.9);
      pop("#p-half", s("07") + 1.6);
      sticker("#p-note", at("07", 0.68));

      // 3 Anki: the card flips to its definition
      tl.fromTo("#card", { rotationY: 0 }, { rotationY: 180, duration: 0.6, ease: MOVE }, s("09") + 0.4);
      sticker("#a-note", s("09") + 1.8);

      // 4 Cambridge: highlight "Evaluate", then stamp it
      tl.fromTo("#c-src", { opacity: 0 }, { opacity: 1, duration: 0.4, ease: "none" }, s("10") + 0.6);
      tl.to("#img-cam", { scale: 1.12, transformOrigin: "0% 55%", duration: 1.0, ease: MOVE }, at("11", 0.3));
      tl.fromTo("#c-hl", { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: MOVE }, at("11", 0.48));
      tl.fromTo("#c-judge", { opacity: 0, scale: 2.2, rotation: -16 }, { opacity: 1, scale: 1, rotation: -8, duration: 0.16, ease: "power4.in" }, e("11") - 0.7);
      shake("#c-judge", e("11") - 0.54);

      // bonus level: a yellow burst, then the three SJ tools
      const bs = s("12") - 0.1;
      tl.fromTo("#bn-bg", { clipPath: "circle(0% at 50% 45%)" }, { clipPath: "circle(120% at 50% 45%)", duration: 0.5, ease: IN }, bs);
      slam("#bn1", bs + 0.15, 1.8);
      tl.fromTo("#bn2", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.4, ease: IN }, bs + 0.6);
      tl.fromTo("#bn-logo", { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.5, ease: POP }, bs + 0.9);
      tl.to("#bn", { opacity: 0, y: -50, duration: 0.25, ease: OUT }, s("13") - 0.3);
      tl.to("#bn-bg", { clipPath: "circle(0% at 50% 45%)", duration: 0.3, ease: OUT }, s("13") - 0.3);

      // 5 Grade Comeback Calculator: each path lights up as it's said, then the answer
      tl.fromTo("#g-c0", { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "none" }, at("13", 0.37));
      tl.to("#g-c0", { opacity: 0, duration: 0.15, ease: "none" }, at("13", 0.58));
      tl.fromTo("#g-c1", { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "none" }, at("13", 0.58));
      tl.to("#g-c1", { opacity: 0, duration: 0.15, ease: "none" }, at("13", 0.8));
      tl.fromTo("#g-c2", { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "none" }, at("13", 0.8));
      tl.to("#g-c2", { opacity: 0, duration: 0.15, ease: "none" }, s("14") + 0.3);
      tl.to("#img-grade", { scale: 1.1, transformOrigin: "20% 50%", duration: 0.8, ease: MOVE }, s("14"));
      pop("#g-ping", s("14") + 0.6);
      sticker("#g-note", s("14") + 1.5);

      // 6 Subject combinations: four steps fill, then the result
      tl.fromTo("#c-steps i", { backgroundColor: "rgba(21,21,21,0.15)" }, { backgroundColor: "#FE6100", duration: 0.12, ease: "none", stagger: 0.18 }, at("15", 0.42));
      tl.fromTo("#img-c1", { opacity: 0 }, { opacity: 1, duration: 0.35, ease: "none" }, at("15", 0.62));
      tl.to("#c-steps", { opacity: 0, duration: 0.2, ease: "none" }, at("15", 0.62));
      sticker("#co-note", at("15", 0.78));

      // 7 Past papers
      tl.to("#img-pp", { scale: 1.06, transformOrigin: "0% 40%", duration: 2.5, ease: "none" }, s("16"));
      tl.fromTo("#pp-free", { opacity: 0, scale: 2.2, rotation: -14 }, { opacity: 1, scale: 1, rotation: -6, duration: 0.16, ease: "power4.in" }, s("16") + 1.45);
      shake("#pp-free", s("16") + 1.61);

      // ---------- Time! The clock freezes, then the 37 tabs, then the end card
      tl.fromTo("#timer", { scale: 1 }, { keyframes: [{ scale: 1.22, duration: 0.12 }, { scale: 1, duration: 0.5, ease: IN }] }, STOP);
      slam("#tm1", STOP + 0.05, 2.0);
      tl.fromTo("#tm2", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.4, ease: IN }, STOP + 0.55);
      tl.to("#tm", { opacity: 0, y: -60, duration: 0.3, ease: OUT }, at("17", 0.38));
      tl.fromTo("#tabs i", { opacity: 0, scaleY: 0 }, { opacity: 1, scaleY: 1, duration: 0.12, ease: "none", stagger: 0.018, transformOrigin: "50% 100%" }, at("17", 0.4));
      tl.fromTo(".send", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.45, ease: IN }, at("17", 0.5));
      tl.fromTo(".endbg", { yPercent: 100 }, { yPercent: 0, duration: 0.5, ease: IN }, END_CARD);
      tl.fromTo("#e-logo", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.5, ease: IN }, END_CARD + 0.25);
      tl.fromTo("#e1, #e2", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.5, ease: IN, stagger: 0.12 }, END_CARD + 0.5);
      sticker("#e3", END_CARD + 1.2);

      // ---------- captions: each chunk pops on and off with its words
      document.querySelectorAll(".cap").forEach((c) => {
        const a = +c.dataset.a, b = +c.dataset.b;
        tl.fromTo(c, { opacity: 0, y: 14, scale: 0.92 }, { opacity: 1, y: 0, scale: 1, duration: 0.14, ease: IN }, a);
        tl.to(c, { opacity: 0, duration: 0.06, ease: "none" }, b - 0.04);
      });

      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = tl;
