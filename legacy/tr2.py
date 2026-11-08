import sys, numpy as np, subprocess
from faster_whisper import WhisperModel
m = WhisperModel("large-v3", device="cpu", compute_type="int8")
def load(a,b,flt):
    return np.frombuffer(subprocess.run(["ffmpeg","-v","error","-ss",str(a),"-to",str(b),"-i",sys.argv[1],"-af",flt,"-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout,np.int16).astype(np.float32)/32768
prompt="GONE.Fludd, рэп, глэм. Пока бокалы полны, у меня нет ни капли уныния. Улицы знают их имена. Глэм до гроба, La Familia."
for a,b in [(3.8,7.6),(12.5,14.4)]:
  for flt in ["anull","highpass=f=200,lowpass=f=4000,volume=2"]:
    for temp in [0.0,0.4]:
      segs,_=m.transcribe(load(a,b,flt),language="ru",beam_size=5,temperature=temp,initial_prompt=prompt,condition_on_previous_text=False)
      print(a,flt[:6],temp,"|"," ".join(s.text for s in segs))
