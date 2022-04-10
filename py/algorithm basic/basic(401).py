# 15988

# 런타임 오류 ... 왜?
# def sol(n):
#     if n<=2:
#         return n
#     elif n==3:
#         return 4
#     else:
#         return sol(n-1)+sol(n-2)+sol(n-3)

# case = int(input())

# for i in range(case):
#     n = int(input())
#     print(sol(n)%1000000009)
    
# 인터넷 방법

# lst = [0] * 1000001
# lst[1], lst[2], lst[3] = 1, 2, 4
# for i in range(4, 1000001):
#     lst[i] = (lst[i-1] + lst[i-2] + lst[i-3]) % 1000000009
# for _ in range(int(input())):
#     num = int(input())
#     print(lst[num])

# 1149

