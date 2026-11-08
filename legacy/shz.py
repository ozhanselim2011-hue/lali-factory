import asyncio,sys,json
from shazamio import Shazam
async def main():
    sh=Shazam()
    for d in sys.argv[1:]:
        best=None
        for st in (2,6,0):
            import subprocess
            subprocess.run(['ffmpeg','-v','error','-y','-ss',str(st),'-t','10','-i',f'{d}/in.mp4','-ac','1','-ar','44100',f'{d}/shz.wav'])
            try:
                import os;r=await sh.recognize(f'{d}/shz.wav',proxy=os.environ.get('HTTPS_PROXY') or os.environ.get('https_proxy'))
            except Exception as e:
                r={'err':str(e)[:80]}
            tr=r.get('track')
            if tr: best=f"{tr.get('subtitle')} — {tr.get('title')}";break
            if 'err' in r: best='ERR '+r['err'];
        print(d,'|',best,flush=True)
asyncio.run(main())
