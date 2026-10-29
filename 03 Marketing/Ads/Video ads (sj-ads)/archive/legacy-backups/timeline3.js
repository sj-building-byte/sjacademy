      const tl = gsap.timeline({ paused: true });
      const E = "expo.out";
      const clipIn = { clipPath: "inset(-10% 100% -10% 0%)" }, clipOut = { clipPath: "inset(-10% 0% -10% 0%)" };


      // slow camera pushes (ease-in-out)
      [["#s1", 0, 3.2], ["#s2", 2.5, 3.6], ["#s3", 5.5, 3.6], ["#s4", 8.5, 3.0], ["#s5", 11.0, 3.2], ["#s6", 13.5, 2.8], ["#s7", 15.5, 3.2], ["#s8", 18.0, 2.0]]
        .forEach(([id, t, d]) => tl.fromTo(`${id} .cam`, { scale: 1 }, { scale: 1.03, duration: d, ease: "sine.inOut", transformOrigin: "50% 45%" }, t));

      // pill: lands once, then stays anchored for the whole film
      tl.set("#pill", { opacity: 1 }, 0);

      // ── S1 hook 0–2.5 ──
      tl.set("#s1 .logo", { opacity: 1 }, 0);
      tl.fromTo("#s1 .h1 .w", { yPercent: 105 }, { yPercent: 0, duration: 0.85, ease: E, stagger: 0.08 }, 0.1);
      tl.fromTo("#s1 .hl .bg", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power3.out" }, 1.3);

      // T1 push up 2.5
      tl.to("#s1", { y: -520, duration: 0.7, ease: "power3.inOut" }, 2.4);
      tl.to("#s1", { opacity: 0, duration: 0.3, ease: "power1.in" }, 2.4);
      tl.fromTo("#s2", { y: 1600 }, { y: 0, duration: 0.95, ease: "power3.inOut" }, 2.4);

      // ── S2 method 2.5–5.5 ──
      tl.set("#s2 .paper", { rotation: -0.6 }, 0);
      tl.fromTo("#s2 .lab .l1", { opacity: 0 }, { opacity: 1, duration: 0.5, ease: E }, 2.75);
      tl.fromTo("#s2 .mark", { opacity: 0, scale: 1.25 }, { opacity: 1, scale: 1, duration: 0.45, ease: E }, 3.25);
      tl.fromTo("#s2 .mnote", clipIn, { ...clipOut, duration: 0.6, ease: "power2.out" }, 3.4);
      tl.to(["#s2 .a1", "#s2 .mark", "#s2 .mnote", "#s2 .lab .l1"], { opacity: 0, duration: 0.25, ease: "power1.out" }, 4.15);
      tl.fromTo("#s2 .lab2", { opacity: 0 }, { opacity: 1, duration: 0.5, ease: E }, 4.25);
      tl.fromTo("#s2 .a2 .al", clipIn, { ...clipOut, duration: 0.45, ease: "power2.out", stagger: 0.08 }, 4.25);
      document.querySelectorAll("#s2 .rt").forEach((sv, i) => tl.set(sv, { opacity: 1 }, [4.55, 4.68, 4.98][i]));
      document.querySelectorAll("#s2 .rt path").forEach((p, i) => tl.fromTo(p, { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.22, ease: "power2.out" }, [4.55, 4.68, 4.98][i]));
      tl.fromTo("#s2 .stamp", { opacity: 0, scale: 1.35, rotation: -14 }, { opacity: 1, scale: 1, rotation: -8, duration: 0.5, ease: "back.out(1.5)" }, 4.95);

      // T2 scale-dissolve 5.5
      tl.to("#s2", { scale: 0.94, duration: 0.4, ease: "power2.in" }, 5.25);
      tl.to("#s2", { opacity: 0, duration: 0.35, ease: "power1.in" }, 5.3);
      tl.fromTo("#s3", { scale: 1.06 }, { scale: 1, duration: 0.85, ease: E }, 5.65);
      tl.fromTo("#s3", { opacity: 0 }, { opacity: 1, duration: 0.35, ease: "power1.out" }, 5.65);

      // ── S3 find your class 5.5–8.5 (real capture) ──
      tl.fromTo("#s3 .sc", { y: 0 }, { y: FIND_END, duration: 1.05, ease: "power2.inOut" }, 5.95);
      tl.fromTo("#s3 .t1", { opacity: 0.9, scale: 0.5 }, { opacity: 0, scale: 1.15, duration: 0.45, ease: "power2.out", immediateRender: false }, 7.05);
      tl.fromTo("#s3 .fo", { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "none" }, 7.1);
      tl.fromTo("#s3 .t2", { opacity: 0.9, scale: 0.5 }, { opacity: 0, scale: 1.15, duration: 0.45, ease: "power2.out", immediateRender: false }, 7.55);
      tl.fromTo("#s3 .ft", { opacity: 0 }, { opacity: 1, duration: 0.15, ease: "none" }, 7.6);

      // T3 slide 8.5
      tl.to("#s3", { x: -1080, duration: 0.8, ease: "power3.inOut" }, 8.45);
      tl.fromTo("#s4", { x: 1080 }, { x: 0, duration: 0.8, ease: "power3.inOut" }, 8.45);

      // ── S4 O Level 8.5–11 ──
      tl.fromTo("#s4 .hl .bg", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power3.out" }, 8.95);
      tl.fromTo("#s4 .oi .wr", clipIn, { ...clipOut, duration: 0.4, ease: "power2.out", stagger: 0.085 }, 9.15);
      document.querySelectorAll("#s4 .oi svg").forEach((sv, i) => tl.set(sv, { opacity: 1 }, 9.4 + i * 0.085));
      tl.fromTo("#s4 .oi path", { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.22, ease: "power2.out", stagger: 0.085 }, 9.4);

      // T4 page-turn 11.0 (the only one)
      tl.set("#s5 .list .wr", clipIn, 0);
      tl.fromTo("#s4 .nb", { rotationY: 0, transformPerspective: 2400 }, { rotationY: -178, transformPerspective: 2400, duration: 0.9, ease: "power2.inOut", transformOrigin: "0% 50%" }, 10.95);
      tl.set(["#s4 .page > *", "#s4 .tabs"], { opacity: 0 }, 11.4);
      tl.to("#s4 .nb", { x: -260, duration: 0.45, ease: "power2.in" }, 11.45);

      // ── S5 A Level 11–13.5 ──
      tl.fromTo("#s5 .hl .bg", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power3.out" }, 11.45);
      tl.fromTo("#s5 .ai .wr", clipIn, { ...clipOut, duration: 0.4, ease: "power2.out", stagger: 0.07 }, 11.6);
      document.querySelectorAll("#s5 .ai svg").forEach((sv, i) => tl.set(sv, { opacity: 1 }, 11.85 + i * 0.07));
      tl.fromTo("#s5 .ai path", { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.22, ease: "power2.out", stagger: 0.07 }, 11.85);

      // T5 slide 13.5
      tl.to("#s5", { x: -1080, duration: 0.8, ease: "power3.inOut" }, 13.45);
      tl.fromTo("#s6", { x: 1080 }, { x: 0, duration: 0.8, ease: "power3.inOut" }, 13.45);

      // ── S6 free tools 13.5–15.5 (real capture) ──
      tl.fromTo("#s6 .lab", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 13.85);
      tl.fromTo("#s6 .sc", { y: 0 }, { y: TOOLS_END, duration: 0.85, ease: "power2.inOut" }, 14.4);

      // T6 brown band rises 15.5
      tl.fromTo("#s7", { y: 1920 }, { y: 0, duration: 0.8, ease: "power3.inOut" }, 15.45);
      tl.to("#s6", { y: -300, duration: 0.8, ease: "power3.inOut" }, 15.45);

      // ── S7 proof 15.5–18 ──
      const count = (id, to, t) => {
        const el = document.getElementById(id), o = { v: 0 };
        tl.to(o, { v: to, duration: 0.9, ease: "power2.out", onUpdate: () => (el.textContent = Math.round(o.v).toLocaleString("en-US")) }, t);
      };
      tl.fromTo("#s7 .n1", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 15.85);
      tl.fromTo("#s7 .l1", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 15.95);
      count("c950", 950, 15.9);
      tl.fromTo("#s7 .n2", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 16.05);
      tl.fromTo("#s7 .l2", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 16.15);
      count("c4500", 4500, 16.1);
      tl.set("#s7 .circ", { opacity: 1 }, 16.8);
      tl.fromTo("#s7 .circ path", { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.5, ease: "power2.inOut" }, 16.8);
      tl.fromTo("#s7 .hr", { scaleX: 0 }, { scaleX: 1, duration: 0.7, ease: E }, 16.85);
      tl.fromTo("#s7 .fact", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out", stagger: 0.09 }, 16.95);

      // T7 yellow band rises 18.0
      tl.fromTo("#s8", { y: 1920 }, { y: 0, duration: 0.8, ease: "power3.inOut" }, 17.95);
      tl.to("#s7 .cam", { y: -300, duration: 0.8, ease: "power3.inOut" }, 17.95);

      // ── S8 close 18–20 ──
      tl.fromTo("#s8 .yl", { opacity: 0, y: -16 }, { opacity: 1, y: 0, duration: 0.8, ease: E }, 18.45);
      tl.fromTo("#s8 .line .w", { yPercent: 105 }, { yPercent: 0, duration: 0.85, ease: E, stagger: 0.07 }, 18.35);
      tl.fromTo("#s8 .btn", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8, ease: E }, 18.7);
      tl.fromTo("#s8 .url", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 18.85);
      tl.fromTo("#s8 .legal", { opacity: 0 }, { opacity: 1, duration: 0.8, ease: E }, 18.95);

      window.__timelines["main"] = tl;
