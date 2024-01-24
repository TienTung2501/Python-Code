
if __name__ == "__main__" :
    n = input()
    a = list(map(int, input().split(' ')))
    P = 0
    res = 0
    D = {}
    for i,x in enumerate(a,0) : 
        if x not in D.keys() or D[x] < P : res = max(res,i - P+1)
        else : P = D[x]+1
    print(res)