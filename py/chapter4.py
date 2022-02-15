## 10952

# while(1):
#     a,b= map(int,input().split())
#     if a==0 and b==0:
#         break        
#     print(a+b)

## 10951

# while True:
#     try:
#         a,b =map(int,input().split())
#         print(a+b)
#     except:
#         break

## 1110
# 시간초과...
# num = int(input())
# time = 0

# while(1):
#     sum = (num//10) + (num%10)
#     new_sum = (num%10)*10 + (sum%10)
#     time += 1
#     if num == new_sum:
#         break
# print(time)

# n = int(input())
# m =n
# count =0

# while True:
#     plus = (n//10) + (n%10)
#     new_n = ((n%10)*10) + (plus%10)
#     count += 1
#     n = new_n
#     if m == new_n:
#         break
# print(count)

