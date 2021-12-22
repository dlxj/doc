
import os,sys,subprocess

out_bytes = subprocess.check_output([r"node", "hira.js", "では ここで問題です"])

out_text = out_bytes.decode('utf-8')

print( out_text.strip() )
