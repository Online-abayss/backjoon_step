## 15596

# def test(n):
#     abc = sum(n)
#     return abc

## 4673

# def test(n):
#     abc = list(str(n))
#     for i in range(0,len(abc)):
#         n += int(abc[i])
#     return n 

# count =[]
# for i in range(1,10000):
#     count.append(test(i))
#     if i not in count:
#         print(i)
    
## 1065 

# def d(n):
#     count = 0
#     if n < 100:
#         return(n)
#     else:
#         for i in range(100,n+1):
#             test = list(map(int,str(i)))
#             if test[0]-test[1] == test[1]-test[2]:
#                 count +=1
#         return(count+99)

# abc = int(input())
# print(d(abc))
