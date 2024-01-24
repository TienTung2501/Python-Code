from queue import PriorityQueue
if __name__ == '__main__':
    L = PriorityQueue()
    R = PriorityQueue()
    n = int(input())
    for i,x in enumerate(map(int,input().split()),1):       
        if (i %2 == 1) : L.put(-x)
        else : R.put(x)
        if i > 1 and -L.queue[0] > R.queue[0] : 
            a = L.get()
            b = R.get()
            R.put(-a)
            L.put(-b)
        print(-L.queue[0], end=" ")
            
        
