import math
p,s = input().split()
p,s = float(p), float(s)
p/=4
d = p**2 - s 
a = p - math.sqrt(d)
b = p + math.sqrt(d)
print(" %8.2f  %8.2f"%(a,b))
