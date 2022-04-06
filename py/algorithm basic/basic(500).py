# 2309

# p_list = []

# for i in range(9):
#     p = int(input())
#     p_list.append(p)

 
# for a in range(8):
#     test = p_list
#     for b in range(a+1,9):
#         if sum(p_list) - (p_list[a]+p_list[b])==100:
#             one = p_list[a]
#             two = p_list[b]
# p_list.remove(one)
# p_list.remove(two)
# p_list.sort()
# for c in p_list:
#     print(c)
            











## 1476

## 각 숫자를 한계에 맞게 나눠서 몫의 값을 얻는다. 15 28 19
## 위의 방식은 16 입력시 나머지 값으로 나올 예정
## 그럼 반대로 하면? 나머지 + 몫*한계값 // 우린 몫을 찾아야한다.
## 1 16 16 -> 1+15*n = 16 // 16+ 28*n // 16+ 19*n을 만족


# earth , sun, moon = map(int,input().split())

# cnt = 1
# while(1):
#     a = cnt %15
#     b = cnt %28
#     c = cnt %19
#     if a ==0:
#         a =15
#     if b ==0:
#         b =28
#     if c ==0:
#         c =19
#     if earth ==a and sun ==b and moon ==c:
#         print(cnt)
#         break
#     cnt +=1
    

# 1107

# 100 > 5457 // 6 7 8 

# 5455 + + > 6
# --
# 100 > 1 // 1 2 3 4 5 6 7 8 9

# 0 + > 2

now_chennel = 100

goal_chennel = int(input())
error_numbers = int(input())

if error_numbers !=0:
    error_key = list(map(int,input().split()))

while(1):
    if goal_chennel == now_chennel:
        print(0)
    




