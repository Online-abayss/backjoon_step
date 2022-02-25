## 1978

## 뭐가 틀린건지 모르겠다.
# n = int(input())

# test = list(map(int,input().split()))

# num = []
# for i in test:
    
#     cnt = 0
#     for j in range(1,test[-1]-1):
#         if i % j == 0:
#             cnt +=1
#     if cnt ==2:
#         num.append(i)

# print(len(num))


#인터넷 방법
# n = int(input())

# test = list(map(int,input().split()))
# cnt = 0
# for i in test:
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break

#         else:
#             cnt += 1

# print(cnt)


## 2581

# M = int(input())
# N = int(input())
# num_list = []
# for i in range(M,N+1):
#     if i>1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             num_list.append(i)
# if sum(num_list)>0:
#     print(sum(num_list))
#     print(num_list[0])
# else:
#     print("-1")


## 11653


## 인터넷 방법.
# for문과 while문을 어찌 줄여야 하는지 너무 고민이었다.. 역시 인터넷짱.
# num = int(input())

# if num == 1:
#     print(' ')

# for i in range(2,num+1):
#     if num%i == 0:
#         while num%i ==0:
#             print(i)
#             num = num//i

## 1929


## 인터넷 방법... 시간초과를 줄일 방법을 못함.
# m,n = list(map(int,input().split()))

# check =  [1 for i in range(n+1)]
# check[0] == 0 , check[1] == 0


# for i in range(2,int(n**0.5)+1):
#     for j in range(i+i,n+1,i):
#         check[j] = 0

# for i in range(m,n+1):
#     if check[i]:
#         print(i)

# 4948

## 인터넷 방법 , 방법은 떠올랏는데 계속 틀려서 포기.
# max_num = 123456*2 +1
# check_list = [1 for i in range(max_num)]

# for i in range(2,int(max_num**0.5)+1):
#     if check_list[i] == 1:
#         j = 2
#         while i*j <=max_num:
#             check_list[i*j] = 0
#             j+=1

# while (1):
#     cnt = 0
#     n = int(input())
#     m = n*2
#     if n == 0:
#         break

#     for i in range(n+1,m+1):
#         if check_list[i]:
#             cnt +=1
#     print(cnt)


## 9020

# n = 10000

# check =  [1 for i in range(n+1)]
# check[0] == 0 , check[1] == 0


# for i in range(2,int(n**0.5)+1):
#     for j in range(i+i,n+1,i):
#         check[j] = 0


# t = int(input())

# for i in range(t):
#     test = int(input())
#     for j in range(test//2,1,-1):
#         if check[j]==1:
#             if check[test-j]:
#                 print(j, test-j)
#                 break



## 1085

# x,y,w,h = map(int,input().split())
# print(min([x,y,w-x,h-y]))


## 3009

## 머리가 안돌아가서 인터넷으로 규칙을 봄.

# X=[]
# Y=[]
# new = []
# for _ in range(3):
#     x, y = map(int,input().split())
#     X.append(x)
#     Y.append(y)
# for i in X:
#     if X.count(i)==1:
#         new.append(i)
# for j in Y:
#     if Y.count(j)==1:
#         new.append(j)
# print(new[0],new[1])

## 인터넷 방법
# X=[]
# Y=[]
# new = []
# for _ in range(3):
#     x, y = map(int,input().split())
#     X.append(x)
#     Y.append(y)

# print(min(X,key=X.count),min(Y,key=Y.count))

## 4153

# while(1):
#     x,y,z = map(int,input().split())
#     num_list = [x,y,z]
#     test = sorted(num_list,reverse=True)
#     if z == y== x ==0:
#         break
#     elif test[0]**2 == (test[1]**2) + (test[2]**2):
#         print("right")
#     else:
#         print("wrong")

## 3053

# import math

# r = int(input())
# print(r*r*math.pi)
# print(r*r*2)


## 1002

# n = int(input())

# for i in range(n):
#   x1, y1, r1, x2, y2, r2 = map(int, input().split())
#   r = ( (x1-x2)**2 + (y1-y2)**2 ) ** (1/2)
  
#   if (r==0 and r1==r2) :
#     print(-1)
#   elif r > (r1 + r2) or r < abs(r1-r2):
#     print(0)
#   elif r == r1+r2 or r == abs(r1-r2) :
#     print(1)
#   else :
#     print(2)
