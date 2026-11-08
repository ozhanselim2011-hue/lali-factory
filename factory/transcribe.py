"""Транскрипция звука с таймкодами слов: python3 factory/transcribe.py jobs/<id>/in.mp4 [model] [prompt]"""
import sys, subprocess, numpy as np
from faster_whisper import WhisperModel
src = sys.argv[1]; model = sys.argv[2] if len(sys.argv) > 2 else "large-v3"
prompt = sys.argv[3] if len(sys.argv) > 3 else None
m = WhisperModel(model, device="cpu", compute_type="int8")
aud = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                                   capture_output=True).stdout, np.int16).astype(np.float32) / 32768
segs, info = m.transcribe(aud, language="ru", word_timestamps=True, vad_filter=False, beam_size=5, initial_prompt=prompt)
for s in segs:
    print(f"[{s.start:5.2f}-{s.end:5.2f}] {s.text.strip()}")
    print("   ", " ".join(f"{w.word.strip()}@{w.start:.2f}" for w in s.words))
