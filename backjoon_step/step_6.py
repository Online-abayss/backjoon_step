# 15596

# def solve(a):
#     ans = sum(a)
#     return ans

# 4673


# # def d(n):
# for n in range(1,30):
#     test = list(str(n))
#     for i in range(0,len(test)):
#         n += int(test[i])
#     print(n)
    
#     # return(result)

# def d(n):
#     test = list(str(n))
#     for i in range(0,len(test)):
#         n += int(test[i])

#     return(n)

# count =[]
# for i in range(1,10000):
#     # for j in range(1,10000): # 이게 필요없는 이유 : 문제상 d(75)= 75 + 7 + 5 즉 무조건 list 추가된 값은 n값보다 크기떄문
#     count.append(d(i))
#     if i not in count:
#         print(i)

         

# 1065
# n = int(input())
# count = 0
# for i in range(1,n+1):
#     test = list(map(int,str(i))) # str(i)로 묶은 이유 : 각 숫자를 하나씩 만들기 위해.
#     if i <100:
#         count += 1
#     else:
#         if test[0]-test[1] == test[1]-test[2]: # 처음엔 한수라는게 각 자릿수 차끼리 같으면 되느줄 알고 abs()라는 절대값을 넣음
#             count += 1

# print(count)

