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
n = input()
test = list(map(int,n))
if n <100:
    print(n)
elif test[0]-test[1] == test[1]-test[2] :
    print(n)