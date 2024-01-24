#http://laptrinhonline.club/problem/tichpxhuffman
from queue import PriorityQueue
import collections
# s = input()
# dic = collections.Counter(s)
# Q = PriorityQueue()
# res = 0
# for x in dic.values(): Q.put(x)
# while Q.qsize() > 1:
#     x = Q.get(-x) + Q.get(-x)
#     res += x
#     Q.put(x)   
# print(res)

# nangcap in ra chuoi ma hoa dung cay (node)
CODE = {}
class node : 
    def __init__(self,c,f,l = None,r = None) :
        self.kt = c
        self.ts = f
        self.left = l
        self.right = r   
    def __lt__(self,other): return self.kt < other.kt

def inorder(h,q = ""):
    if h == None: return 
    inorder(h.left, q +"\t\t")
    print("%s%s - %d" % (q,h.kt,h.ts))
    inorder(h.right, q +"\t\t")

def getcode(h, q ="") :
    if h.left == None : CODE = print(h.kt, q)
    else :
        getcode(h.left, q + "0")
        getcode(h.right, q + "1")
        
if __name__ == '__main__':
    s = input()
    Q = PriorityQueue()
    dic = collections.Counter(s)
    for k,v in dic.items(): Q.put(node(k,v))
    
    while Q.qsize() > 1:
        u = Q.get()
        v = Q.get()
        Q.put(node('$', u.ts  + v.ts, u,v))
    root  = Q.get()
    inorder(root)
    getcode(root)
              