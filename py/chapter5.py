## 10818

# num = int(input())
# nlist = list(map(int,input().split()))
# print(min(nlist),max(nlist))
    
## 2562

# nlist = []

# for i in range(9):
#     nlist.append(int(input()))
# print(max(nlist))
# print(nlist.index(max(nlist))+1)

## 2577

# nsum  = int(input())*int(input())*int(input())
# for i in range(10):
#     print(str(nsum).count(str(i)))

## 3052

# test = []
# for i in range(10):
#     test.append((int(input())%42))
# print(len(set(test)))

## 1546


# nsum = 0
# count = int(input())
# test = list(map(int,input().split()))
# M = max(test)
# for i in range(count):
#     nsum += int(test[i])
# fakenum = nsum/int(M)*100/count
# print("%.2f"%fakenum)

            ## 의문증 test = 란에(34줄) list 안박고 그냥 input().split 박아서 type 확인해보니 list여서 했는데 왜 안되는지 모르겠다.

## 8958

# num = int(input())

# for i in range(num):
#     count = 0
#     sum = 0
#     check = list(input())
#     for j in check:
#         if j == "O":
#             count +=1
#             sum += count
#         else:
#             count = 0
#     print(sum)

## 4344

# num = int(input())

# for i in range(num):
#     avg = 0
#     count = 0
#     case = list(map(int,input().split()))
#     avg = (sum(case)-case[0])/case[0]
#     for j in range(1,case[0]+1): 
#         if case[j]>avg:
#             count +=1
#     print("%.3f"%((count/case[0])*100)+'%')
