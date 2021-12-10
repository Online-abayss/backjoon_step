# 내가 이해한 수학문제들만..

#1712

# a,b,price = map(int,input().split())

# count = 0

# if b >= price:
#     print(-1)
# else:
#     count = a//(price-b)
#     print(count+1)

#2869


# 초과시간 생각 안하고 반복문 할 경우
# a,b,v = map(int,input().split())
# day=0
# while v >(a-b)*day + a:
#     day+=1    
#     if v<=(a-b)*day +a:
#         break
# print(day+1)

# 인터넷 방법. ceil는 소수점일경우 올림해서 정수
# import math
# a,b,v = map(int,input().split())

# day = (v-a)/(a-b) + 1 
# print(math.ceil(day))

#만약 math 함수 안쓰고싶으면. 올림만 하면되는거니깐. int형은 정수형이니 if문해서 같으면 그대로 아니면 +1 하는 형식으로 하면 될듯.

