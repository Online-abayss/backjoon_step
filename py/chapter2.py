## 1330

# a,b = map(int,input().split())

# if a>b:
#     print(">")
# elif a==b:
#     print("==")
# else:
#     print("<")


## 9498

# a= int(input())

# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# else:
#     print("F")

## 2753
# a= int(input())

# if a%4 == 0 and a%100 != 0 or a%400 ==0:
#     print("1")
# else:
#     print("0")

##
# a= int(input())
# b= int(input())

# if a>0 and b>0:
#     print("1")
# elif a>0 and b<0:
#     print("4")
# elif  a<0 and b>0:
#     print("2")
# else:
#     print("3")

    ## 인터넷방법
    # a = int(input())
    # b = int(input())
    # if a > 0:
    #     print(1 if b > 0 else 4)
    # elif a < 0:
    #     print(2 if b > 0 else 3)

## 2884 

# h , m = map(int,input().split())
# if m >=45:
#     print(h, m-45)
# elif h> 0 and m <45:
#     print(h-1, m+15)
# else:
#     print(23,m+15)

## 2525

#왜 틀린지 모르겠다... 결과값은 나오는데..
# h, m = map(int,input().split())
# ing = int(input())
# sumH = (m+ing)//60
# sumM = (m+ing)%60

# if h+sumH >23:
#     print("{} {}".format(0,sumM))
# else:
#     if m+ing<60:
#         print("{} {}".format(h,m+ing))
#     if m+ing>=60:
#         print("{} {}".format(h+sumH,sumM))

#인터넷 맞는 답.
# H, M = map(int, input().split())
# timer = int(input()) 

# H += timer // 60
# M += timer % 60

# if M >= 60:
#     H += 1
#     M -= 60
# if H >= 24:
#     H -= 24

# print(H,M)

## 2480

#왜 틀린지 또 모르겠다.
# a,b,c = map(int,input().split())
# if a!=b!=c:
#     print(max(a,b,c)*100)
# elif a==b==c:
#     print(10000+a*1000)
# else:
#     if a==c:
#         print(1000+a*100)
#     if b==c:
#         print(1000+b*100)
#     if a==b:
#         print(1000+a*100)

## 인터넷 답
# a, b, c = map(int, input().split())

# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(100 * max(a,b,c))
    

