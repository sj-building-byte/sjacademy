# Generates a soothing 120 bpm (half-time feel) bed with local MusicGen. Deterministic seed.
import torch, numpy as np, soundfile as sf, sys
from transformers import AutoProcessor, MusicgenForConditionalGeneration
torch.manual_seed(21)
out = sys.argv[1]
name = "facebook/musicgen-medium"
proc = AutoProcessor.from_pretrained(name)
model = MusicgenForConditionalGeneration.from_pretrained(name).to("mps" if torch.backends.mps.is_available() else "cpu")
prompt = ("soothing warm felt piano with soft ambient pads and gentle muted plucks, calm and hopeful, "
          "light brushed percussion, steady gentle pulse at 120 bpm with a relaxed half-time feel, clean mix, no vocals")
inp = proc(text=[prompt], padding=True, return_tensors="pt").to(model.device)
with torch.no_grad():
    a = model.generate(**inp, do_sample=True, guidance_scale=3.5, max_new_tokens=int(24 * 50))
sr = model.config.audio_encoder.sampling_rate
w = a[0, 0].float().cpu().numpy(); w = w / (np.abs(w).max() + 1e-9) * 0.9
sf.write(out, w, sr); print("wrote", out, len(w) / sr)
