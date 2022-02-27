## 10872

# def N(num):
#     sum = 1
#     if num>0:
#         sum = num * N(num-1)
#     return sum

# print(N(int(input())))

## 10870

# def fibo(n):
#     sum = 0
#     if n >1:
#         sum = fibo(n-2) + fibo(n-1)
#     elif n ==1:
#         sum = 1

#     return sum

# print(fibo(int(input())))

## 2448

## 문제만 봣을때 이해는 안됫다. 인터넷 보고 이해함.

# num = int(input())

# def print_stars(n):
#     if n ==3:
#         return ['***','* *','***']

#     stars = print_stars(n//3)
#     arr = []
#     for star in stars:
#         arr.append(star*3)
#     for star in stars:
#         arr.append(star+' '*(n//3)+star)
#     for star in stars:
#         arr.append(star*3)
#     return arr

# print('\n'.join(print_stars(num)))




## 11729

## 하노이탑 공식 Tn = 2^n -1

# def hanoi(n,start,mid,to):
    
#     if n == 1:
#         print(start, to)
#     else:
#         hanoi(n-1, start , to, mid)
#         print(start, to)
#         hanoi(n-1, mid ,start,to)

# n = int(input())

# print((2**n)-1)
# hanoi(n,1,2,3)
    
