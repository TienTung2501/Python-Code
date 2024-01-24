###### CAU TRUC RE NHANH
# test 1 : in ra chu cai tiep theo duoi dang viet thuong
# c =input()
# if c == 'z' or c == 'Z' :print('a')
# else : 
#     tmp = ord(c)
#     tmp+=1
#     print(chr(tmp).lower())


# test 2 : kiem tra chu hoa hay thuong
# c = input()
# if c.islower(): print('lower')
# elif c.isupper(): print('upper')
# elif c.isdigit(): print('digit')
# else : print('special')\
    
    
#test 3 : chuyen doi in hoa hay in thuong, ko phai chu thi giu nguyen
# c = input()
# if c.islower(): print(c.upper())
# elif c.isupper(): print(c.lower())
# else : print(c)


# test 4 : domino (cho 1 hinh chu nhat M x N ben trong laf cac hinh vuong , vo so cac thanh domino 2x1) xep duoc bao nhieu domino
# m,n = map(int,input().split())
# res = 0
# if n %2 == 0 : res = (n/2)* m
# else : res = ((n-1)//2)*m + m//2
# print(res)


# test 5 :  lat da quang truong mxn , da co kich thuoc axa, tim so da it nhat
# m,n,a = list(map(int,input().split()))
# if m%a > 0 : k =(m//a)+1
# else : k = m//a
# if n%a > 0 : t =(n//a)+1
# else : t = n//a
# print(t*k)


#test 6 : frog 1 con ech nhay theo quy tac sau trong he truc toa do
# buoc nhay thu nhat a don vi ve phia ben phai
# buoc nhay thu hai la b don i ve trai , roi lap lai nhu v
# neu con ech nhay mot so lan chan truoc lan nhay hien tai thi thi no nhay tu x => x + a,: else thi nhay tu x => x - b
# Tinh toan vi tri cua x sau k buoc nhay
# coi x = 0     ----------x-----------
# a,b,k = list(map(int,input().split()))
# left, right = 0,0
# if k %2 == 0 :
#     left = k//2
#     right = k //2
# else : left = k//2 ; right = left +1

# print(right*a - left*b)


#test 7 : co vo so dong su menh gia tu 1,2...n chonj 1 bo so co tong tien  = s,  tim so luong duong du min
# n,s = map(int,input().split())
# if s %n == 0: print (s//n)
# else : print (s//n +1)


# test 8 :  doraemon leo cau thang co n buoc, moi lan lan leo len chi leo dc 1 hay 2 bac, dorae mon muon so la di chuyen la boi so cua so nguyen n
# tim so lan di chuyen min, neu ko co cach nao thi in ra -1
m,n = map(int,input().split())
res = 0
if m % 2 == 0 : res = m//2
else : res = m//2 +1
if (res < n) : print(n)
else : 
    if res % n == 0 : print(res)
    else : print((res//n + 1) *n)

