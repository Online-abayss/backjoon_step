## 2798

# n, m = map(int,input().split())

# num_list = list(map(int,input().split()))
# result = 0

# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             num_sum = num_list[i]+num_list[j]+num_list[k]
#             if num_sum <=m:    
#                 result = max(num_sum,result)

# print(result)
            

## 2231

# n = int(input())

# for i in range(n):
     
#      total = i
#      for j in range(len(str(i))):

#           total += int(str(i)[j])
#      if total == n:
#           print(i)
#           break
# else:
#      print(0)


## 7568

## 인터넷의 힘.

# case = int(input())
# student_list = []
# for _ in range(case):
#     weight, height = map(int,input().split())
#     student_list.append((weight, height))
# for one in student_list:
#     rank = 1
#     for other in student_list:
#         if one[0]<other[0] and one[1] <other[1]:
#          rank += 1
#     print(rank,end =" ")

    # 인터넷방법 2

# n = int(input())
# lst = [list(map(int, input().split())) for i in range(n)]
# ans = [1 for i in range(n)]
# for i in range(n):
#     cnt = 0
#     for j in range(n):
#         if i == j:
#             continue
#         if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
#              cnt += 1
#     ans[i] += cnt
# for i in ans:
#     print(i, end = ' ')
            ## 2차원 리스트로 한 방법이며, text[][] 일경우 앞의 [] 는 [[1,2,3],[4,5,6]] 이라는 2차원 배열에서 큰 리스트 단위 순서를 표현, 뒷 [] 는 그 큰 리스트안에서의 리스트 순서이다.
                # 즉 text[1][2]라면, text[1]이 나왓기에 [4,5,6]리스트가 결정되며, [2]도 있기에, [4,5,6]중에 인덱스가 2인 6이 정해진다. 


## 1436

# num = int(input())
# test = 665
# cnt = 0
# while(1):
#     test +=1
#     test_list = list(str(test))
#     if test_list.count('6')>=3: 
#         for i in range(len(test_list)-2): ## 여기다가 -2 한 이유 : test_list[i+2]를 했기에, -2가 없으면 최대 길이가 3인 구간에서 없는 5를 요청해서 오류발생.
#             if test_list[i] == test_list[i+1] == test_list[i+2] == '6':
#                 cnt +=1
#                 break
#     if num == cnt:
#         print(test)
#         break

# 첫번째로 잘못한점. 6이 3번만 있으면되는게 아니라 연속해서 3번이 필요함. 그러므로 if test_list.count('6')>=3: 이 식은 잘못됨.


## 인터넷 방법 [ 아 개 노가다 했는데, 역시 쉬운방법이 존재하구만... ]
# n = int(input())
# number = 666
# cnt = 0

# while 1:
#     if '666' in str(number):
#         cnt += 1
#     if cnt == n:
#         print(number)
#         break
#     number +=1




# 666 / 1 ,2,3,4,5, 6660, 6661~9 , 7666


