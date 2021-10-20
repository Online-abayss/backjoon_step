#10952.......

# while True:
#     a,b = map(int,input().split())
#     if a ==0 and b==0:
#         break
#     print(a+b)

#10951
# 이 문제는 while문을 진행하여, EOF(End Of File) 즉 예기치 못한 상황으로 파일이 끝날 경우 진행하는 방법을 문제로 제시함

#----인터넷 방법 1 ----
# try:
#     while True:
#         a,b = map(int,input().split())
#         print(a+b)


# except:
#     print("")

#---- 인터넷 방법 2 ----
# while True:
#     try:
#         a,b =map(int,input().split())
#         print(a+b)
#     except:
#         break

#1110
n = int(input())
m =n
count =0

while True:
    plus = (n//10) + (n%10)
    new_n = ((n%10)*10) + (plus%10)
    count += 1
    n = new_n
    if m == new_n:
        break
print(count)


# https://blog.naver.com/yardyard/222455656176