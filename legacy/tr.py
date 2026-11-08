import sys
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[2], device="cpu", compute_type="int8")
import numpy as np, subprocess
aud = np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout, np.int16).astype(np.float32)/32768
segs, info = m.transcribe(aud, language="ru", word_timestamps=True, vad_filter=False, beam_size=5)
for s in segs:
    print(f"[{s.start:5.2f}-{s.end:5.2f}] {s.text.strip()}")
    print("   ", " ".join(f"{w.word.strip()}@{w.start:.1f}" for w in s.words))
