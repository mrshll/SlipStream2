class uniquify():
    def uni_ord(self, seq, idfun=None):
       # order preserving
       if idfun is None:
           def idfun(x): return x
       seen = {}
       result = []
       for item in seq:
           marker = idfun(item)
           # in old Python versions:
           # if seen.has_key(marker)
           # but in new ones:
           if marker in seen: continue
           seen[marker] = 1
           result.append(item)
       return result
    def interleave(self, xs, ys):
        result = []
        for i in range(0, min(len(xs), len(ys))):
            result.append(xs[i])
            result.append(ys[i])
        return result
