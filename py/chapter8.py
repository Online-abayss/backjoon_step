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


## 10250 


# # 왜 틀린지 모르겠다. 일단 원하는 값은 다 나온다. // 찾았다... room_list = [] 를 for문 안으로 집어 넣어야 했다. , list를 리셋 해줘야 했었나 보다.
# case = int(input())


# for o in range(case):
#     room_list = []
#     H, W, N = list(map(int,input().split()))

#     for i in range(1,W+1):

#         for j in range(1,H+1):
#             room_num = 100*j+i ## 여길 str(h) + str(w).zfill(2) 이라는 zfiil 함수 이용하는 방법도 있다. zfill이란 str의 문자를 전체 문자열길이()에 맞추기 위해 필요시 앞에 0이 붙는다. 
#             room_list.append(room_num)
#     print(int(room_list[N-1]))


##  2775

# 0층의 i호수는 i 만큼 산다.
# k층의 1호수는 1명만 산다.
# k층의 n 호수는 k-1층의 n 호수의 합만큼 산다. / k층의 n = k-1층의 n의 합.

#인터넷 방법.
# T = int(input())
# for i in range(T):
#     floor = int(input())
#     room = int(input())
#     people = [j for j in range(1,room+1)] ## 이걸 풀이하면 j값을 리스트 한개씩 넣는 형식.
#     for k in range(floor):
#         for m in range(room-1):
#             people[m+1] += people[m] # k가 0일시 그냥 j입력된 리스트 호출, 아닐시 덮어쓰기처럼 
#     print(people[-1]) ## 리스트 맨 마지막을 불러오기.
# print(people)

## 2839


# 너무 복잡해져서 인터넷 힘을 빌림.)
# n = int(input())
# f = n//5
# n %=5
# t = 0

# while f >=0:
#     if n%3 ==0:
#         t = n//3
#         n = n%3
#         break
#     f-=1        
#     n+=5
# print((n==0) and (f+t)or -1) ## if를 쓴것처럼 표현 가능.

## 10757

# A,B = map(int,input().split())

# print(A+B)


