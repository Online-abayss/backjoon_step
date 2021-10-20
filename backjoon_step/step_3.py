#2739
# num = int(input())
# for i in range(1,10):
    # print("{} * {} = {}".format(num,i,num*i))
    # print(num,"*",i,"=",num*i)
    # print(num+"*"+i+"="+num*i)   # +는 문자끼리면 연결해주나봄.

#10950
# a = int(input())

# for i in range(a):
#     num1,num2 = map(int,input().split())
#     print(num1+num2)

# 위에 것보다 밑에것이 실행속도가 빠른 코드 ( 인터넷에 찾아본거지만, 왜그런지는 모르겠다.)
# t = int(input())
# i = 0
# a = [] ; b=[]
# while(i<t):
#     ta,tb = map(int,input().split())
#     a.append(ta)
#     b.append(tb)
#     i +=1
# i = 0
# while(i<t):
#     print(a[i]+b[i])
#     i += 1

#8393
# sum = 0
# a = int(input())
# for i in range(a+1):
#     sum = sum + i # sum += i
# print(sum)

#15552
# import sys

# repeat = int(input())
# for i in range(repeat):
#     a , b = map(int,sys.stdin.readline().split())
#     print(a+b)

#2741

# num = int(input())
# for i in range(1,num+1):
#     print(i)

#2742

# num = int(input())
# for i in reversed(range(1,num+1)):
#     print(i)

#11021

# import sys
# repeat = int(input())
# for i in range(1,repeat+1):
#     a,b = map(int,sys.stdin.readline().split())
#     print("Case #{}: {}".format(i,a+b))

#11022
# repeat = int(input())
# for i in range(1,repeat+1):
#     a,b = map(int,input().split())
#     print("Case #{}: {} + {} = {}".format(i,a,b,a+b))

#2438
# n = int(input())
# for i in range(1,n+1):
#     print("*"*i)


#2439
# n= int(input())
# for i in reversed(range(n)):
#     print(" "*i+"*"*(n-i))

# --- f-string 함수의 정렬방법. 한번쯤 알아보는것도 좋을듯. 
# n= int(input())
# for i in range(1,n+1):
#     print(f'{"*"*i:>{n}}') # f" ~{}"의 형식 :>{}는 우측정렬을 {}안의 숫자만큼 옮겨서 쓰라는 뜻.  


#10871

# n , x = map(int,input().split())
# a = []
# a = input().split()
# for i in range(len(a)):
#     if int(a[i])<x:
#         print(a[i],end=" ")


