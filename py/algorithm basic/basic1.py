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

