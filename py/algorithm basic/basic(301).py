# 9613

## 인터넷방법
# import sys
# def gcd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a%b)
# T = int(sys.stdin.readline())
# for t in range(T):
#     cnt = 0
#     a = list(map(int, sys.stdin.readline().split()))
#     for i in range(1, a[0]):
#         for j in range(i+1, a[0]+1):
#             cnt += gcd(a[i], a[j])
#     print(cnt)


# 17087





## 1373

## 시간초과
# def test(n,k):
#     answer = ''

#     while n>0:
#         n,mod = divmod(n, k)
#         answer += str(mod)
#     return answer[::-1]

# print(test(int(input(),2),8))

# n= int(input(),8)
# print(oct(n)[2:])

# 1212

# n= int(input(),8)
# print(bin(n)[2:])

#2089

# 이해가 안되서 인터넷봄
# N=int(input()) 
# ans='' 
# if N==0: 
#     print(0) 
#     exit() 
# while N!=0: 
#     if N%-2: 
#         N=N//-2+1 
#         ans='1'+ans 
#     else: 
#         N//=-2 
#         ans='0'+ans 
# print(int(ans))

## 17103

