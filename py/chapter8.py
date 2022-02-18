## 1712

# a,b,c = map(int,input().split())

# if b >=c:
#         print("-1")
# else:
#        print(int(a/(c-b)+1))


## 2292

# num = int(input())
# start = 1
# cnt = 1 
# while num > start:
#         start += 6*cnt ## 벌집이 6n씩 증가.
#         cnt +=1
# print(cnt)

## 1193

# def sum_n(n): # 각 항의 합의 갯수
#         sum =0
#         for i in range(1,n+1):
#                 sum += i 
#         return sum
 

# test = int(input())

# cnt =0
# while(1):  # 그룹을 1 (홀)/ 23 (짝)/ 456 (홀)/ 78910 (짝)/ 등으로 나누어서 몇번째 그룹인지 찾기.
#      cnt += 1
#      if test <= (cnt*(cnt+1))/2: ## 끝 자락이 1 ,3 ,6 , 10 , 15 즉 1부터의 합을 말함
#              break
# num = int(test - (cnt*(cnt-1))/2) ## 그 그룹에서  몇번째 항인지 알려고. (10 - 6) = 4

# if (cnt % 2 == 0):
#         print("{}/{}".format(num,(cnt-num+1)))

# else:
#         print("{}/{}".format((cnt-num+1),num))

## 인터넷 방법

# x=int(input())
# l=1

# while x>l:
#     x-=l
#     l+=1
# if l%2==0:
#     a=x
#     b=l-x+1
# else:
#     a=l-x+1
#     b=x
    
# print(a,'/',b,sep='')

## 2869

# up , down , height = list(map(int,input().split()))

# start = 0
# day = 0
# while(1):
#         day += 1
#         start += up
#         if start >= height:
#                 print(day)
#                 break
#         start -= down

# import math

# up , down , height = list(map(int,input().split()))

# day = (height-up)/(up-down) + 1
# print(math.ceil(day))


