# 1463




# n = int(input())
# d = [0] * (n + 1)	## d에 계산된 값을 저장해둔다. n + 1이라고 한 이유는, 1번째 수는 사실 d[1]이 아니고 d[2]이기 때문에, 계산하기 편하게 d[1]을 1번째 인 것 처럼 만들어준다.

# for i in range(2, n + 1):
# ## 여기서 왜 if 1빼는 방법, 2 나누기, 3 나누기 동등하게 하지 않고 처음에 1을 빼고 시작하는지 의아해 할 수 있다.
# ## 1을 빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문이다.
# ## 즉 셋 다 시도하는 방법이 맞다.

# ## 여기서 if elif else를 사용하면 안된다. if만 이용해야 세 연산을 다 거칠 수 있다, 가끔 if continue, else continue를 쓰는 분도 계신데, 난 이게 편한듯.
#     d[i] = d[i - 1] + 1
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)	## 1을 더하는 것은 d는 결과가 아닌 계산한 횟수를 저장하는 것 이기 때문이다. d[i]에는 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기 때문이다.
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
# print(d[n])


# 11726


## 인터넷 방법 / 규칙이 1,2,3,5,8 으로 가는 그 규칙이였다..
# n = int(input())

# d = [0 for _ in range(n+1)]

# if n<=3:
#     print(n)
# else:
#     d[1]=1
#     d[2]=2
#     for i in range(3,n+1):
#         d[i] = d[i-1]+d[i-2]
#     print(d[i]%10007)


# 11727

# n = int(input())

# d = [0 for _ in range(n+1)]

# if n<=1:
#     print(n)
# elif n==2:
#     print(n+1)
# else:
#     d[1]=1
#     d[2]=3
#     for i in range(3,n+1):
#         d[i] = d[i-1]+d[i-2]*2
#     print(d[i]%10007)

# 9095

## 런타임 오류 왜 뜨는지 모름 실행은 잘되는데.
# case = int(input())

# for a in range(case):

#     num = int(input())
#     d = [0 for _ in range(num+1)]

#     if num<=2:
#         print(n)
#     elif num==3:
#         print(4)
#     else:
#         d[1]=1
#         d[2]=2
#         d[3]=4
#         for i in range(4,num+1):
#             d[i] = d[i-1] + d[i-2] + d[i-3]
#     print(d[num])

# case = int(input())

# def sol(n):
#     if n<=2:
#         return n
#     elif n==3 :
#         return 4
#     else:
#         return sol(n-3)+sol(n-2)+sol(n-1)

# for i in range(case):
#     n = int(input())
#     print(sol(n))

# 11052


## 인터넷 방법
# n = int(input())
# p = list(map(int, input().split()))
# p.insert(0,0)
# dp = [0 for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1,i+1):
#         dp[i] = max(dp[i], p[j] + dp[i-j])
# print(dp[n])
    
        



# import sys

# input = sys.stdin.readline
# test_sum = 0
# case = int(input())
# for i in range(1,case+1):
#     test_sum += len(str(i))
# print(test_sum)



import sys

input = sys.stdin.readline

case = int(input())

