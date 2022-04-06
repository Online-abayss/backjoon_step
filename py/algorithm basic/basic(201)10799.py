## 17413

# word = input() + ' '
# temp = ''
# idx = 0
# while idx < len(word):
#     if word[idx] == ' ':
#         print(temp[::-1], end=' ')
#         temp = ''
#     elif word[idx] == '<':
#         print(temp[::-1], end='')
#         temp = ''
#         next_tag = word.find('>', idx)
#         print(f'{word[idx:next_tag + 1]}', end='')
#         idx = next_tag
#     else:
#         temp += word[idx]
#     idx += 1


## 10799

# bar_razor = list(input())
# answer = 0
# stack = []

# for i in range(len(bar_razor)):
#     if bar_razor[i] == '(': #
#         stack.append('(')
        
#     else:
#         if bar_razor[i-1] == '(': 
#             stack.pop()
#             answer += len(stack)
            
#         else:
#             stack.pop() 
#             answer += 1 

# print(answer)

# 17298

## 시간초과
# case = int(input())

# nums = list(map(int,input().split()))


# for i in range(case):
#     if i == case-1:
#         print(-1)
#         break
#     elif max(nums[i:]) > nums[i]:
#         for j in range(i+1,case):
#             if nums[j] > nums[i]:
#                 print(nums[j], end= " ")
#                 break
            
#     else:
#         print(-1, end= " ")


# https://my-coding-notes.tistory.com/82

# import sys
# input = sys.stdin.readline

# n = int(input())
# seq = list(map(int,input().split()))
# stack = []

# for i in range(n):
#     while(stack):
#         if seq[i] > seq[stack[-1]]:
#             seq[stack.pop()] = seq[i]
#         else:
#             stack.append(i)
#             break
    
#     if not stack:
#         stack.append(i)
# for i in stack:
#     seq[i] = -1
    
# print(*seq)