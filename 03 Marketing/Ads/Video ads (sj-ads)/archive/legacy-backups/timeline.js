      const tl = gsap.timeline({ paused: true });
      const S = (sel) => document.querySelectorAll(sel);

      // ── camera push on every scene ────────────────────────────────────────
      [["#s1", 0, 2.2], ["#s2", 1.8, 2.9], ["#s3", 4.3, 2.9], ["#s4", 6.8, 2.9], ["#s5", 9.3, 3.4], ["#s6", 12.3, 3.5], ["#s7", 15.2, 2.8]].forEach(
        ([id, t, d]) => tl.fromTo(`${id} .cam`, { scale: 1 }, { scale: 1.06, duration: d, ease: "sine.inOut" }, t),
      );

      // ── S1 · 0–2s · brand reveal (legible from frame 0, already moving) ──
      tl.fromTo("#s1 .sun", { y: -40, scale: 1 }, { y: 140, scale: 1.12, duration: 2.2, ease: "none" }, 0);
      tl.fromTo("#s1 .ring", { x: 0, y: 0 }, { x: 90, y: -200, duration: 2.2, ease: "none" }, 0);
      tl.fromTo("#s1 .yr", { x: 60 }, { x: -120, duration: 2.2, ease: "none" }, 0);
      tl.fromTo("#s1 .plate", { scale: 0.92, rotation: -2 }, { scale: 1, rotation: 0, duration: 0.7, ease: "back.out(2.4)" }, 0);
      tl.fromTo("#s1 .k1", { x: -40 }, { x: 0, duration: 0.6, ease: "power3.out" }, 0);
      tl.fromTo(
        "#s1 .big .ch",
        { y: (i) => (i % 2 ? 16 : -16), rotation: (i) => (i % 2 ? 3 : -3) },
        { y: 0, rotation: 0, duration: 0.7, ease: "back.out(2.6)", stagger: 0.035 },
        0,
      );
      tl.fromTo("#s1 .bar", { scaleX: 0.8, transformOrigin: "0% 50%" }, { scaleX: 1, duration: 0.6, ease: "back.out(2)" }, 0.05);
      tl.fromTo("#s1 .mq", { x: 0 }, { x: -700, duration: 2.2, ease: "none" }, 0);
      tl.to("#s1 .big", { scale: 1.035, transformOrigin: "0% 50%", duration: 0.12, ease: "power2.out", yoyo: true, repeat: 1 }, 1.0);
      tl.to("#s1 .bar", { scale: 1.04, transformOrigin: "0% 50%", duration: 0.12, ease: "power2.out", yoyo: true, repeat: 1 }, 1.5);

      // ── S2 · 2–4.5s · hook ────────────────────────────────────────────────
      tl.fromTo("#s2 .ghost", { y: 120, scale: 0.9 }, { y: -80, scale: 1.05, duration: 2.9, ease: "none" }, 1.8);
      tl.fromTo("#s2 .gt1", { y: 0, rotation: -10 }, { y: 160, rotation: 8, duration: 2.9, ease: "none" }, 1.8);
      tl.fromTo("#s2 .gt2", { y: 0, rotation: 6 }, { y: -220, rotation: -6, duration: 2.9, ease: "none" }, 1.8);
      tl.fromTo("#s2 .k2", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, 1.95);
      tl.fromTo("#s2 .hl .w", { yPercent: 115 }, { yPercent: 0, duration: 0.45, ease: "back.out(1.7)", stagger: 0.11 }, 1.95);
      tl.fromTo("#s2 .mk .tx", { color: "#F7F5EF" }, { color: "#453516", duration: 0.2, ease: "none", stagger: 0.25 }, 2.8);
      tl.fromTo("#s2 .mk .hi", { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power3.out", stagger: 0.25 }, 2.72);
      tl.to("#s2 .mk2", { scale: 1.09, transformOrigin: "0% 50%", duration: 0.14, ease: "power2.out", yoyo: true, repeat: 1 }, 3.5);
      tl.to("#s2 .mk1", { scale: 1.06, transformOrigin: "0% 50%", duration: 0.14, ease: "power2.out", yoyo: true, repeat: 1 }, 3.0);
      tl.fromTo("#s2 .bt path", { strokeDasharray: 80, strokeDashoffset: 80 }, { strokeDashoffset: 0, duration: 0.3, ease: "power2.out" }, 3.5);
      tl.fromTo("#s2 .bt", { rotation: -8, scale: 0.9 }, { rotation: 0, scale: 1, duration: 0.6, ease: "back.out(2)" }, 3.5);
      tl.fromTo("#s2 .sub", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 3.4);

      // ── S3 · 4.5–7s · O Level poster stack ────────────────────────────────
      tl.fromTo("#s3 .blob", { y: -60, scale: 0.9 }, { y: 120, scale: 1.1, duration: 2.9, ease: "none" }, 4.3);
      tl.fromTo("#s3 .lab", { scale: 1.5, opacity: 0, transformOrigin: "0% 100%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(1.8)" }, 4.32);
      tl.fromTo("#s3 .k3", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.35, ease: "power3.out" }, 4.5);
      tl.fromTo("#s3 .ol-w", { x: (i) => (i % 2 ? 1100 : -1100) }, { x: 0, duration: 0.42, ease: "expo.out", stagger: 0.075 }, 4.45);
      tl.fromTo("#s3 .ol-n", { opacity: 0 }, { opacity: 1, duration: 0.2, ease: "none", stagger: 0.075 }, 4.5);
      tl.fromTo("#s3 .scan", { opacity: 0, y: 0 }, { opacity: 1, duration: 0.06, ease: "none" }, 5.7);
      S("#s3 .ol-w").forEach((el, i) => {
        const t = 5.7 + i * 0.09;
        if (i > 0) tl.set("#s3 .scan", { y: i * 104 }, t);
        tl.set(el, { color: "#FCE004" }, t);
        tl.set(el, { color: i % 2 ? "#8A3A00" : "#453516" }, t + 0.09);
      });
      tl.set("#s3 .scan", { opacity: 0 }, 5.7 + 12 * 0.09);
      tl.to("#s3 .stack", { y: -18, duration: 2.5, ease: "none" }, 4.5);

      // ── S4 · 7–9.5s · A Level tag drop ────────────────────────────────────
      const rot = [-5, 4, -3, 6, -4, 3, -6, 2, 5, -3, 4, -5];
      tl.fromTo("#s4 .disc", { rotation: 0, x: 0 }, { rotation: 30, x: 120, duration: 2.9, ease: "none" }, 6.8);
      tl.fromTo("#s4 .lab", { scale: 0.5, opacity: 0, transformOrigin: "0% 50%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, 6.85);
      tl.fromTo("#s4 .k4", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.35, ease: "power3.out" }, 7.05);
      tl.fromTo(
        "#s4 .al-tag",
        { y: -1500, rotation: (i) => rot[i] * 5 },
        { y: 0, rotation: (i) => rot[i], duration: 0.5, ease: "back.out(1.5)", stagger: 0.055 },
        6.82,
      );
      tl.to("#s4 .al-tag", { y: (i) => (i % 2 ? -12 : 12), duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 1, stagger: 0.03 }, 8.35);
      tl.fromTo("#s4 .as", { xPercent: 30, opacity: 0 }, { xPercent: 0, opacity: 1, duration: 0.5, ease: "expo.out" }, 8.0);

      // ── S5 · 9.5–12.5s · method: marked paper → classroom ─────────────────
      tl.fromTo("#s5 .glow", { scale: 0.8, y: 60 }, { scale: 1.1, y: -60, duration: 3.4, ease: "none" }, 9.3);
      tl.fromTo("#s5 .hd .w", { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "back.out(1.6)", stagger: 0.06 }, 9.4);
      tl.fromTo(
        "#s5 .paper",
        { y: 260, rotation: -9, scale: 0.88, opacity: 0 },
        { y: 0, rotation: -2.5, scale: 1, opacity: 1, duration: 0.6, ease: "back.out(1.3)" },
        9.4,
      );
      tl.fromTo("#s5 .tick path", { strokeDasharray: 80, strokeDashoffset: 80 }, { strokeDashoffset: 0, duration: 0.22, ease: "power2.out", stagger: 0.25 }, 10.0);
      tl.fromTo("#s5 .note", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.5)", stagger: 0.25 }, 10.05);
      tl.fromTo("#s5 .score", { scale: 2.2, opacity: 0, rotation: -25 }, { scale: 1, opacity: 1, rotation: -8, duration: 0.35, ease: "back.out(2)" }, 10.85);
      tl.fromTo("#s5 .pnote", { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: 0.3, ease: "power3.out" }, 10.75);
      tl.fromTo("#s5 .sub .w", { yPercent: 60, opacity: 0 }, { yPercent: 0, opacity: 1, duration: 0.35, ease: "back.out(1.8)", stagger: 0.07 }, 10.5);
      tl.to("#s5 .paper", { y: -160, scale: 0.8, rotation: -6, opacity: 0, duration: 0.35, ease: "power3.in" }, 11.15);
      tl.fromTo(
        "#s5 .photo",
        { clipPath: "circle(0% at 50% 50%)" },
        { clipPath: "circle(75% at 50% 50%)", duration: 0.6, ease: "power3.inOut" },
        11.3,
      );
      tl.fromTo("#s5 .photo img", { scale: 1.2 }, { scale: 1.02, duration: 1.4, ease: "power2.out" }, 11.3);
      tl.fromTo("#s5 .cap", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }, 11.75);

      // ── S6 · 12.5–15.5s · proof count-ups ─────────────────────────────────
      tl.fromTo("#s6 .blob", { y: 80, scale: 0.9 }, { y: -100, scale: 1.08, duration: 3.5, ease: "none" }, 12.3);
      tl.fromTo("#s6 .row", { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.6)", stagger: 0.5 }, 12.4);
      const counter = (id, to, start, fmt) => {
        const el = document.getElementById(id);
        const o = { v: 0 };
        tl.to(o, { v: to, duration: 0.85, ease: "power3.out", onUpdate: () => (el.textContent = fmt(o.v)) }, start);
        tl.to(`#${id}`, { scale: 1.08, transformOrigin: "0% 60%", duration: 0.1, ease: "power2.out", yoyo: true, repeat: 1 }, start + 0.85);
      };
      counter("n1", 950, 12.45, (v) => `${Math.round(v)}+`);
      counter("n2", 4500, 12.95, (v) => `${Math.round(v).toLocaleString("en-US")}+`);
      counter("n3", 5, 13.45, (v) => v.toFixed(1));
      tl.fromTo("#s6 .stars svg", { scale: 0, rotation: -60 }, { scale: 1, rotation: 0, duration: 0.3, ease: "back.out(3)", stagger: 0.06 }, 13.85);
      tl.fromTo("#s6 .tl", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 14.1);
      tl.fromTo("#s6 .pill", { scale: 0.4, opacity: 0, y: 60 }, { scale: 1, opacity: 1, y: 0, duration: 0.4, ease: "back.out(2.4)", stagger: 0.18 }, 14.3);

      // ── S7 · 15.5–18s · close ─────────────────────────────────────────────
      tl.fromTo("#s7 .c1", { y: 0, rotation: 0 }, { y: -160, duration: 2.8, ease: "none" }, 15.2);
      tl.fromTo("#s7 .c2", { y: 0, x: 0 }, { y: 140, x: -60, duration: 2.8, ease: "none" }, 15.2);
      tl.fromTo("#s7 .hl .w", { yPercent: 115 }, { yPercent: 0, duration: 0.45, ease: "back.out(1.7)", stagger: 0.11 }, 15.3);
      tl.fromTo("#s7 .plate", { scale: 0.7, opacity: 0, transformOrigin: "0% 50%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }, 16.2);
      tl.fromTo("#s7 .adm", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 16.5);
      tl.fromTo("#s7 .mode", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 16.7);
      tl.fromTo("#s7 .url", { scale: 0.5, opacity: 0, transformOrigin: "0% 50%" }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.4)" }, 17.0);
      tl.fromTo("#s7 .demo", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 17.15);
      tl.to("#s7 .url", { scale: 1.05, duration: 0.12, ease: "power2.out", yoyo: true, repeat: 1 }, 17.5);

      // ── film grain: deterministic jitter, 12 steps per second ─────────────
      for (let i = 0; i < 216; i++) tl.set("#grain", { x: ((i * 37) % 60) - 30, y: ((i * 53) % 60) - 30 }, i / 12);

      // ── shader transitions between scenes (cuts on the 120 bpm grid) ──────
      HyperShader.init({
        bgColor: "#453516",
        accentColor: "#FCE004",
        scenes: ["s1", "s2", "s3", "s4", "s5", "s6", "s7"],
        transitions: [
          { time: 1.8, shader: "flash-through-white", duration: 0.4 },
          { time: 4.3, shader: "cinematic-zoom", duration: 0.4 },
          { time: 6.8, shader: "whip-pan", duration: 0.4 },
          { time: 9.3, shader: "cinematic-zoom", duration: 0.4 },
          { time: 12.3, shader: "flash-through-white", duration: 0.4 },
          { time: 15.25, shader: "sdf-iris", duration: 0.5 },
        ],
        timeline: tl,
      });
      window.__timelines["main"] = tl;
