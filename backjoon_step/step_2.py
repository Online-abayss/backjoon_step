
#1330

# a , b = map(int,input().split())

# if a > b:
#     print(">")
# elif a <b:
#     print("<")
# else:
#     print("==")

#9498

# a = int(input())
# if a >= 90:
#     print("A")
# elif a >= 80:
#     print("B")
# elif a >= 70:
#     print("C")
# elif a >= 60:
#     print("D")
# else:
#     print("F")

#2753
# a = int(input())

# if (a%4)==0 and not (a%100)==0:
#     print("1")
# elif(a%400)==0:
#     print("1")
# else:
#     print("0")

#--- 간략된 버전 ---
# a = int(input())

# if (a%4==0 and a%100 !=0) or a%400 ==0:
#     print("1")
# else:
#     print("0")

# #14681
# x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print("1")
# elif x<0 and y>0:
#     print("2")
# elif x<0 and y<0:
#     print("3")
# else:
#     print("4")


# 2884
# h , m = map(int,input().split())
# if m >=45:
#     print(h, m-45)
# elif h> 0 and m <45:
#     print(h-1, m+15)
# else:
#     print(23,m+15)