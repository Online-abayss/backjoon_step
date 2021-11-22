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


#2577
# print(150*266*427)

# test = []
# test = str(150*266*427)
# print(test)
# print(test.index('0')) # 내가 착각하고 있었던것. index는 특정값이 몇번쨰 인덱스에 있는지 알려주는것, 그래서 내가 원하는 3개의 값이 아닌 170 0이 인덱스2에 있기에 2를 출력.
# for i in range(len(test)):
#     print(test.count(str(i)))
    
# A = int(input())
# B = int(input())
# C = int(input())

# mult_result = list(str(A*B*C))
# for i in range(len(mult_result)+2): # 아니 내가 이렇게 한거랑 그냥 range(10)이랑 뭔 차이가 있길레 내가 쓴건 틀리고 10한건 맞는거지? 결과값이 17037300 길이는 8자이며, +2 하면 10으로 같을테고
#     print(mult_result.count(str(i))) # 실행값은 같은데 왜 내껀 틀리고, 다른 방식의 값은 맞게 된건지 모르겠네;


#3052
# count = []
# for i in range(1,11):
#     num = int(input())%42
#     count.append(str(num))
#     if count.count(str(num)) >1:
#         count.remove(str(num)) # pop도 될듯.
# print(len(count))


#---- 인터넷 방법 ----
# arr = []
# for i in range(10):
#         n = int(input())
#         arr.append(n % 42)
# arr = set(arr) # set 함수는 중복 제거 ( 집합에서의 중복 제거.)
# print(len(arr))

#1546 # 문제를 이해못함;; 


#8958


# n = int(input())
test = list(map(str,input()))
count = 1
sum = 0
a = list("O")

for i in range(len(test)):
    if test[0] == "O":
        sum =+ count
    elif i>0:
        if test[i] == "O":
            if test[i] == test[i-1]:
                    count = count + 1
                    sum = sum + count

            else:
                count = 1
                sum = sum + count
    print(test[i])
    print(type(test[i]))



# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX