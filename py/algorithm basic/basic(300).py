## 2609

## 인터넷 좀 봄
# a, b = map(int, input().split())
# key, x, y = 1, 1, 1
# min = a if a < b else b
# for i in range(1, min+1):
#     if a % i == 0 and b % i == 0:
#         key = i
#         x = a / i
#         y = b / i
# print(key)
# print(int(x * y * key))

    
## 1934

# case = int(input())


# key, w, e = 1 , 1 , 1

# for _ in range(case):
#     a, b = map(int,input().split())
#     for i in range(1,min(a,b)+1):
#         if a % i == 0 and b % i == 0:
#             key = i
#             x = a / i
#             y = b / i
    
#     print(int(key*x*y))

        ## math.lcm(a,b) -> 최소 공배수 / math.gcd(a,b) -> 최대 공약수 방법도 있다고 합니다.



## 1929

# import sys

# m, n = map(int, sys.stdin.readline().split())
# answer = [1] * (n + 1)
# answer[0], answer[1] = 0, 0

# for i in range(2, int(n ** 0.5) + 1):
#     for j in range(i + i, n + 1, i):
#         answer[j] = 0

# for i in range(m, n + 1):
#     if answer[i]:
#         print(i)


## 6588








## 1676

def fac(n):
        fac_sum = 1
        if n > 0:
                fac_sum = n * fac(n-1)
        return fac_sum

num = fac(int(input()))
cnt = list(str(num))

count = 0
for i in range(len(cnt)):
        if cnt[-1] == "0":
                count +=1
                cnt.pop()
        else:
                break
print(count)




