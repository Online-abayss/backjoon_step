#10818

# n = int(input())
# nums = input().split() # 이걸로 실행시 type은 list / 추측하기엔 입력받은 값을 nums에 list로 저장하나봄
# nums=10,20,30 # 이걸로 실행시 tpye은 tuple / 변수명 = (입력값) 으로 안해도 알아서 ()넣은걸로 인식해서 저장하나봄 <- 찾아보니 그렇다고 한다.
# print(type(nums))

# print(list(nums))

# print(min(nums),max(nums)) # 왜 옆의 문장처럼 min 함수랑 max 함수를 같이 쓰면 안되는가.
# print(nums) # 위의 의문점에 대한 해결은 내가 nums = map(~~~~)로 설정하였으며, 이때 tpye을 확인해보면 map으로 뜬다.. 즉.. list가 아니다.
# map은 내장함수로. 정수형이든 원하는 타입으로 변형 해주는 함수다.
# print(min(nums))

# n = int(input())
# nums = list(map(int,input().split()))
# print(min(nums),max(nums))

#2562
# n=[] 
# for i in range(9):
#     a = input() 
#     n.append(a)
# print(n)
# print(max(n))
# print(n.index(max(n))+1)

# n = []
# for i in range(9):
#     n.append(int(input()))
# print(max(n))
# print(n.index(max(n))+1)

print(150*266*427)

