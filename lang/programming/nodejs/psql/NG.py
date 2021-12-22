
import re

def NG(strs):
    strs = re.sub(r"\s+", "", strs, flags=re.UNICODE)

    def ng(s, n):
  
      grs = []
  
      #for (i = 0; i < s.length; i++):
      for i in range(len(s)):
  
        if ( i + n > len(s) ):
          break
  
        gr = s[i:i+n]
  
        grs.append(gr)
  
      return grs


    gss = []
    for i  in range(2, 10):
      gs = ng(strs, i)
  
      if (len(gs) > 0):
  
        gss = gss + gs
  
      else:
        break
  
    return " ".join(gss)
  
NG(' ab cdefg')

