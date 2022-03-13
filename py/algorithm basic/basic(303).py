## 11005

# system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
# N, B = map(int, input().split())
# answer = ''

# while N != 0:
#     answer += str(system[N % B]) 
#     N //= B
    
# print(answer[::-1])

## 2745

# a, b = input().rstrip().split()
# print(int(a, int(b)))

## 11576
## 인터넷 봄.

# x, y = map(int, input().split())
# z = int(input())
# a = list(map(int, input().split()))
# ten = 0
# answer =[]
# for i in range(z):
#     ten += a[-1] * (x**i)
#     a.pop(-1)
# while ten !=0:
#     answer.append(str(ten % y))
#     ten = ten // y

# print(' '.join(answer[::-1]))






