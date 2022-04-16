# 2558

# a = int(input())
# b = int(input())
# print(a+b)


# 3046

# r1,s = map(int,input().split())

# print((2*s)-r1)

# 2163

# r1,s = map(int,input().split())

# print(r1*s-1)

# 10699

# import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d'))

# 2530

# h,m,s = map(int,input().split())

# sec = int(input())

# s1 = (s+sec)%60 
# m1 = (s+sec)//60

# m2 = (m+m1)%60 
# h1 = (m+m1)//60

# h2 = (h+h1)%24 

# print(h2,m2,s1)  

# 2914

# a, b = map(int,input().split())

# print(a*(b-1)+1)

# 5355

# @ = *3 / % = +5 / # = -7


# case = int(input())
# for i in range(case):
    
#     test = list(input().split())
#     sum_test = float(test[0])
#     for j in range(1,len(test)):
#         if test[j] == '@':
#             sum_test *= 3
#         elif test[j] == '%':
#             sum_test += 5
#         elif test[j] == '#':
#             sum_test -= 7
#     print(f'{sum_test:.2f}')


# 2935

# a = int(input())
# op = input()
# b = int(input())
# if op == '*':
#     print(a * b)
# else:
#     print(a + b)

# 10817

# test = list(map(int,input().split()))

# test.remove(max(test))
# print(max(test))

# 1789

# max_num = int(input())
# i = 0
# while(1):
#     if max_num<0:
#         print(i-2)
#         break
#     max_num -= i
#     i += 1

# 10039

# score = []
# for _ in range(5):
#     test_score = int(input())
#     if test_score <40:
#         test_score = 40
#     score.append(test_score)
# print(int(sum(score)/5))
    
# 10156

# snack, n , money = map(int,input().split())

# if snack*n-money <=0:
#     print(0)
# else:
#     print(snack*n-money)

# 2476

# case = int(input())
# answer = 0

# for _ in range(case):
#     a, b, c = map(int, input().split())
    
#     if a == b == c:
#         answer = max(answer, 10000+a*1000)
#     elif a == b:
#         answer = max(answer, 1000+a*100)
#     elif a == c:
#         answer = max(answer, 1000+a*100)
#     elif b == c:
#         answer = max(answer, 1000+b*100)
#     else:
#         answer = max(answer, 100 * max(a,b,c))

# print(answer)


# 4101

# while(1):
#     a,b = map(int,input().split())
#     if a==b==0:
#         break
#     if a>b:
#         print('Yes')
#     elif a<=b:
#         print('No')
    
# 2754

# GPA = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
#        'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
#        'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
#        'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
#        'F': 0.0}
# print(GPA[input()])

# 4375


# while(1):
#     try:
#         n = int(input())

#     except EOFError:
#         break
#     if n== 1:
#         print(1)
#         continue
#     num = 1
#     cnt = 1
#     while(1):
#         num = num * 10 +1
#         cnt +=1
#         if (num%n)==0:
#             print(cnt)
#             break
        

# 1037

# case = int(input())

# nums= list(map(int,input().split()))

# if len(nums) ==1:
#     print(nums[0]*nums[0])
# else:
#     print(max(nums)*min(nums))


# 17427


# n = int(input())

# n_sum=0
# for i in range(1,n+1):
    
#     n_sum += (n//i)*i
# print(n_sum)

# 17425

#시간초과
# case = int(input())

# for _ in range(case):
#     n = int(input())
#     n_sum=0
#     for i in range(1,n+1):
        
#         n_sum += (n//i)*i
#     print(n_sum)

# 7567

# dish = list(str(input()))
# answer = 0

# for i in range(len(dish)):
#     if i == 0:
#         answer += 10
#     elif dish[i] == dish[i-1]:
#         answer += 5
#     else:
#         answer += 10
        
# print(answer)

# 5063

# for _ in range(int(input())):
#     r , e , c = map(int,input().split())
#     if e-c > r:
#         print('advertise')
#     elif e-c == r:
#         print('does not matter')
#     else:
#         print('do not advertise')

# 10102

# case = int(input())

# cnt_a , cnt_b = 0,0

# test = list(input())
# for i in range(case):
#     if test[i] == 'A':
#         cnt_a +=1
#     elif test[i] =='B':
#         cnt_b +=1
# if cnt_a > cnt_b:
#     print("A")
# elif cnt_a == cnt_b:
#     print("Tie")
# else:
#     print("B")

# 10886

# case = int(input())
# answer = []
# for i in range(case):
#     answer.append(int(input()))
# if answer.count(1) > answer.count(0):
#     print('Junhee is cute!')
# else:
#     print('Junhee is not cute!')


# 10988

# word = input()
# if word == word[::-1]:
#     print('1')
# else:
#     print('0')

# 5086



# while(1):
#     a, b = map(int,input().split())
#     if a == b == 0:
#         break
#     if b % a ==0:
#         print('factor')
#     elif a % b ==0:
#         print('multiple')
#     else:
#         print('neither')


# 5717

# while(1):
#     a, b = map(int,input().split())
#     if a==b==0:
#         break
#     print(a+b)

# 9610

# case = int(input())
# Q1 = Q2 = Q3 = Q4 = AXIS = 0

# for _ in range(case):
#     x, y = map(int, input().split())
#     if x == 0 or y == 0:
#         AXIS += 1
#     elif x > 0 and y > 0:
#         Q1 += 1
#     elif x < 0 and y > 0:
#         Q2 += 1
#     elif x < 0 and y < 0:
#         Q3 += 1
#     elif x > 0 and y < 0:
#         Q4 += 1

# print("Q1: %d" %(Q1))
# print("Q2: %d" %(Q2))
# print("Q3: %d" %(Q3))
# print("Q4: %d" %(Q4))
# print("AXIS: %d" %(AXIS))
    





# 9085


# case = int(input())
# for i in range(case):
#     T = int(input())
#     nums = map(int,input().split())
#     print(sum(nums))

# 9506

# while True:
#     n = int(input())
#     if n == -1: # 입력 값이 -1이면 반복문 종료
#         break
#     arr = []
#     for i in range(1, n):
#         if n % i == 0:
#             arr.append(i)
#     if sum(arr) == n:
#         print(n, " = ", " + ".join(str(i) for i in arr), sep="")
#     else:
#         print(n, "is NOT perfect.")
            


## 10162

# A = 5분 / B = 1분 / C = 10초

# a,b,c = 0,0,0
# t = int(input())

# if t%10 !=0:
#     print(-1)
# else:
#     a = t//300
#     b = (t%300)//60
#     c = ((t%300)%60)//10

#     print(a, b , c, sep=" ")


# 10103

# case = int(input())

# player1, player2 = 100, 100
# for i in range(case):
#     a, b  = map(int,input().split())
#     if a > b :
#         player2 -= a
#     elif a < b :
#         player1 -= b
#     else:
#         continue
# print(player1,player2 ,sep="\n" )


# 10214

# case = int(input())

# Y  , K = 0 ,0
# for _ in range(case):
#     for i in range(9):
#         a , b = map(int,input().split())
#         Y +=a
#         K +=b
#     if Y  > K :
#         print('Yonsei')
#     elif Y < K :
#         print('korea')
#     else:
#         print('Draw')

# 11557

# case = int(input())

# S = []
# L = []
# for i in range(case):

#     for j in range(int(input())):
#         a, b  = input().split()
#         S.append(a)
#         L.append(int(b))
#     print(S[L.index(max(L))])


# 1977


m = int(input())
n = int(input())


cnt = []
for i in range(1,101):
    if n >= i**2 >= m :
        cnt.append(i**2)
if len(cnt) == 0:
    print(-1)
else:
    print(sum(cnt),min(cnt), sep='\n')









