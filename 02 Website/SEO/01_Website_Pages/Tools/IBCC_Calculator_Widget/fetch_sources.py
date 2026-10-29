from pathlib import Path
import urllib.request, concurrent.futures, subprocess
from pypdf import PdfReader
urls={
'2021-o':'equivalence/2021-O-Levels.pdf','2021-a':'equivalence/2021-A-Level.pdf',
'2022-o':'equivalence/2022-O-Levels.pdf','2022-a':'equivalence/2022-A-Level.pdf',
'2023-o':'equivalence/O-Levels.pdf','2023-a':'equivalence/A-Level-.pdf',
'2024-o':'wp-content/uploads/2025/08/O-Levels-2024.pdf','2024-a':'wp-content/uploads/2025/06/A-Levels-2024.pdf',
'2025-o':'wp-content/uploads/2025/10/O-Level-2025.pdf','2025-a':'wp-content/uploads/2025/06/A-Levels-2025.pdf',
'2026-o':'wp-content/uploads/2026/07/O-Level-2026.pdf','2026-a':'wp-content/uploads/2026/07/A-Levels-2026.pdf'}
p=Path(__file__).parent/'sources'
def fetch(k,v):
 try:
  f=p/(k+'.pdf'); subprocess.run(['curl','-fLsS','--max-time','30','https://ibcc.edu.pk/'+v,'-o',str(f)],check=True)
  t='\n'.join(x.extract_text() for x in PdfReader(f).pages)
  (p/(k+'.txt')).write_text(t)
  return k+'\n'+t
 except Exception as e: return k+' ERROR '+str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for r in pool.map(lambda kv: fetch(*kv),urls.items()): print(r)
