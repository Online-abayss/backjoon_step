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

#11729

def hanoi(n):
    