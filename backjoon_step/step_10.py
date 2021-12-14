#10872
# 뭣도 모르고 for문으로 쓴 나
# a=1
# for n in range(1,int(input())+1):
#    a*=n 

# print(a)

# 백준이 원하는 for문 안쓰고 하는법.
# def test(n):
#     sum = 1
#     if n> 0:
#         sum = n * test(n-1)
#     return sum

# n = int(input())
# print(test(n))

# 10870

# def test(n):
#     sum = 1
#     if n>2:
#         sum = test(n-1)+test(n-2)
#     if n ==0:
#         sum=0
#     return sum
# n = int(input())
# print(test(n))


# 11729

# def hanoi(n,a,b,c):
#     if n==1:
#         print(a,c) # 이동할 원판 즉 마지막 원판이며, 가장 큰 원판일것이니 1>3으로 이동
#     else:
#         hanoi(n-1,a,c,b) # 하나 남을때까지 통채로 1>2로 옮기는 작업. 
#         print(a,c) #if와 동일.
#         hanoi(n-1,b,a,c) # 다시 2에 있는 것들을 c에 옮기는 작업.

# 인터넷 보고 이해함. 하노이의 논리?를 

