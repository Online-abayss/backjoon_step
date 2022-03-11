## 1935










# 10808

# alpha = 'abcdefghijklmnopqrstuvwxyz'
# lst = [0]*len(alpha)

# text =input()

# for i in range(len(alpha)):
#     lst[i] = text.count(alpha[i])

# print(*lst) ## 앞에 * 붙이면 list로 표현되던게 평범한 문장 호출로 바뀐다.


## 10820
## A 65 Z 90 a 97 z 122

## 왜 오류인지 모름 잘되는데.
# while(1):
    
#     text = input() 

#     if not text:
#         break
#     cnt_A = 0
#     cnt_a = 0
#     cnt_int = 0
#     cnt_space = 0
#     for i in text:
#         if 90 >= ord(i) >= 65:
#             cnt_A += 1
#         elif 122 >= ord(i) >= 97:
#             cnt_a += 1
#         elif i == " ":
#             cnt_space +=1
#         else:
#             cnt_int += 1
#     print(f"{cnt_a} {cnt_A} {cnt_int} {cnt_space}")

## 인터넷 방법 .이건 왜 런타임 오류 안뜨는지 모르겠다. ㅡㅡ
# while True:
#   try:
#     lower = 0
#     upper = 0
#     num = 0
#     space = 0
#     n = list(input())
#     for j in range(len(n)):
#       if n[j].islower():
#         lower += 1
#       elif n[j].isupper():
#         upper += 1
#       elif n[j] == ' ':
#         space += 1
#       else:
#         num += 1
#     print(lower, upper, num, space)
#   except EOFError:
#     break

## 2743

# print(len(input()))

## 11655

# text = input()
# temp = []
# for i in text:
#     if i.isupper():
#         if ord(i) +13 <=90:
#             temp.append(chr(ord(i)+13))
#         else:
#             temp.append(chr(ord(i)-13))
#     elif i.islower():
#         if ord(i) +13 <=122:
#             temp.append(chr(ord(i)+13))
#         else:
#             temp.append(chr(ord(i)-13))
#     else:
#         temp.append(i)
# print("".join(temp))

## 10824

# a,b,c,d = input().split()

# sum_a = a+b
# sum_c = c+d

# print(int(sum_a)+int(sum_c))

## 11656

# text = input()

# lst = []

# for i in range(len(text)):
#         lst.append(text[i:])
# lst.sort()
# print(*lst, sep="\n")
