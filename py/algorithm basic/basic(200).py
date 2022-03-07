## 10828

# import sys

# input = sys.stdin.readline

# n = int(input())

# lst = []

# for _ in range(n):
#     word = input().split()
#     order = word[0]

#     if order == "push":
#         num = word[1]
#         lst.append(num)
#     elif order == "pop":
#         if len(lst) == 0:
#             print(-1)
#         else:
#             print(lst.pop())
#     elif order == "size":
#         print(len(lst))
#     elif order == "empty":
#         if len(lst) == 0:
#             print(1)
#         else:
#             print(0)
#     elif order == "top":
#         if len(lst) == 0:
#             print(-1)
#         else:
#             print(lst[-1])

## 9093

# import sys

# input = sys.stdin.readline

# case = int(input())

# text_list = []

# for _ in range(case):
#     text_list = input().split()
#     for i in range(len(text_list)):
#         print(text_list[i][::-1], end=" ")


## 9012

# import sys
# input = sys.stdin.readline

# case = int(input())

# for _ in range(case):
#     check_list = []
#     text_list = list(map(str,input().rstrip()))
#     for i in text_list:
#         if len(check_list) == 0 :
#             check_list.append(i)
#         elif check_list[0] == i:
#             check_list.append(i)
#         elif check_list[0] == ")" and i == "(":
#             break
#         else:
#             check_list.pop(0)
#     if len(check_list) == 0:
#         print("YES")
#     else:
#         print("NO")

## 1874

## 인터넷방법 1[출력초과됨..] 
# n=int(input())
# result=[]
# nums=[]
# num=1
# for i in range(n):
#     a=int(input())
    
#     while num<=a:
#         result.append("+")
#         nums.append(num)
#         num+=1
#     if nums[-1]==a:
#         result.append("-")
#         nums.pop()
#     else:
#         print("NO")
#         break
# print("\n".join(result))



## 인터넷 방법2 
# import sys
# input = sys.stdin.readline

# N = int(input())

# str1 = [] # 수열
# str2 = [] # 스택

# num = 1
# flag = 1

# for i in range(N):
#     n = int(input())
#     while num <= n:
#         str1.append(num)
#         str2.append('+')
#         num +=1
#     if str1[-1] ==n:
#         str1.pop()
#         str2.append('-')
#     else:
#         flag = 0
# if flag ==0:
#     print("NO")
# else:
#     for i in str2:
#         print(i)


## 1406


## 시간초과. [ 사유 : insert 쓰면 오래 걸리나봄.]
# import sys
# input = sys.stdin.readline

# text = list(map(str,input().strip()))

# case = int(input())


# cursor = len(text)

# for i in range(case):
#     order = list(map(str,input().strip()))
    
#     if order[0] == "L":
#         if cursor == 0 :
#             continue
#         else:
#             cursor -= 1
#     if order[0] == "D":
#         if cursor == len(text):
#             continue
#         else:
#             cursor += 1
#     if order[0] == "B":
#         if cursor == 0 :
#             continue
#         else:
#             cursor -=1
#             text.pop(cursor)
#     if order[0] == "P":
#         text.insert(cursor, order[2])
#         cursor +=1
# print("".join(text))

## 인터넷 방법  / 따로 배열을 둬서 합치기...
# import sys
# input = sys.stdin.readline
# string = list(input().strip()) # 기존 문자열을 받아온다
# result = []
# n = int(input()) # 명령의 개수를 저장한다
# for i in range(n):
#     command = input().strip() # 0번째는 커맨드, 2는 삽입할 문자
#     if command[0]=='P':
#         string.append(command[2])
#     elif command[0]=='L' and string!=[]: # string 이 비어있다면 넘길수 없다
#         result.append(string.pop()) # 커서가 왼쪽으로 움직였다면 기존 스트링에서 마지막 데이터를 다른 리스트로 넘긴다
#     elif command[0]=='D' and result!=[]: # result 가 비어있다면 넘길수 없다
#         string.append(result.pop()) # 커서가 오른쪽으로 움직였다면 기존 스트링에 다른 리스트의 마지막 데이터를 넘긴다
#     elif command[0]=='B' and string!=[]: # string 이 비어있다면 pop 할 수 없다
#         string.pop() # 없애는 거라면 그냥 기존 리스트에서 제거한다
# print(''.join(string+list(reversed(result))))

## 10845

# import sys

# input = sys.stdin.readline

# case = int(input())

# qu = []
# for _ in range(case):
#     word = input().split()
#     order = word[0]
#     if order == "push":
#         qu.append(word[1])
#     elif order == "pop":
#         if len(qu) == 0:
#             print(-1)
#         else:
#             print(qu.pop(0))
#     elif order == "size":
#         print(len(qu))
#     elif order =="empty":
#         if len(qu) ==0:
#             print(1)
#         else:
#             print(0)
#     elif order == "front":
#         if len(qu) ==0:
#             print(-1)
#         else:
#             print(qu[0])
#     elif order == "back":
#         if len(qu) ==0:
#             print(-1)
#         else:
#             print(qu[-1])

## 1158

## 인터넷 방법 1

# import sys

# n, k = map(int, sys.stdin.readline().split())
# stack = [i for i in range(1, n + 1)]
# answer = []
# cnt = k - 1

# while stack:
#     if cnt < len(stack):
#         answer.append(stack.pop(cnt))
#         cnt += k - 1

#     else:
#         cnt %= len(stack)

# print("<", ", ".join(str(i) for i in answer), ">", sep="")

# ## 인터넷 방법 2 ## 겨우 이해는 했지만 못만들겟다.
# N,K = map(int,input().split())
# arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

# answer = []   # 제거된 사람들을 넣을 배열
# num = 0  # 제거될 사람의 인덱스 번호

# for t in range(N):
#     num += K-1  
#     if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
#         num = num%len(arr)
 
#     answer.append(str(arr.pop(num)))
# print("<",", ".join(answer)[:],">", sep='')

# # num 2 // 3기입  // arr [1,2,4,5,6,7] // num 4  // 6 기입 //

## 10866

# import sys
# from collections import deque
# input=sys.stdin.readline
# N = int(input()) # 명령의 수
# dq = deque()
# for _ in range(N) :
#     Order = list(input().split())
#     if Order[0] == "push_front" :
#         dq.appendleft(Order[1])
#     elif Order[0] == "push_back" :
#       dq.append(Order[1])
#     elif Order[0] == "pop_front" :
#         if len(dq) == 0 :
#             print(-1)
#         else :
#             print(dq.popleft())
#     elif Order[0] == "pop_back" :
#         if len(dq) == 0 :
#           print(-1)
#         else :
#           print(dq.pop())
#     elif Order[0] == "size" :
#         print(len(dq))
#     elif Order[0] == "empty" :
#         if len(dq) == 0 :
#            print(1)
#         else :
#            print(0)
#     elif Order[0] == "front" :
#         if len(dq) == 0 :
#             print(-1)
#         else :
#              print(dq[0])
#     elif Order[0] == "back" :
#         if len(dq) == 0 :
#             print(-1)
#         else :
#             print(dq[-1])


## deque 매소드.
# 1. append(x) : 요소를 뒤에 삽입

# 2. appendleft(x) : 요소를 앞에 삽입

# 3. extend(iterable) :  추가 삽입해주는 메소드 ( 확장개념)

# 4. extendleft(iterable) : 위와 이하동문 다만 앞에다가 추가 삽입

# 5. pop() : 오른쪽 마지막요소를 제거후 출력(반환)

# 6. popleft() : 왼쪽 마지막요소를 제거후 출력(반환)

# 7. rotate(n) : 요소들의 값만큼 회전시켜주는 메소드


