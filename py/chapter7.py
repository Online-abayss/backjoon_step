## 11654

# print(ord(input()))

## 11720

# count = int(input())
# num = list(map(int,input()))

# print(sum(num))


## 10809
# 97~ 122


# test = input()
# abc = list(range(97,123))
# for i in abc:
#     print(test.find(chr(i)),end= " ")


## 2675

# T = int(input())

# for i in range(T):
#     a,b = input().split()
#     for j in b:
#         print(int(a)*j,end="")
#     print()


# 값은 뜨는데 왜 안되는지 모르겠다. # 댕청미.
# T , R = list(input().split())

# for i in R:
#     print(int(T)*i,end="")

## 1157

# test = input().upper()

# test_set = list(set(test))
# lcnt = []

# for i in test_set:
#     cnt = test.count(i)
#     lcnt.append(cnt)

# if lcnt.count(max(lcnt)) > 1:
#     print("?")
# else:
#     max_index = lcnt.index(max(lcnt))
#     print(test_set[max_index])


## 1152

## 왜 틀린지 모르겠다 오류도 없는데. 백준에서는 틀렸다고 한다...
# test = list(input().upper())

# count = 0

# if test[0] != chr(32) and test[len(test)-1] != chr(32):
#     count = 1
# for i in test:
#     if i== chr(32):
#         count += 1

# print(count)

## 인터넷에 찾은 답.. 간단하네... 
# import sys

# text = list(map(str,sys.stdin.readline().split()))
# print(len(text))

# text = list(input().split())
# print(len(text))

# 아스키코드 공백값 32
# 단어를 대문자로 바꾸기
# 단어 len으로 반복 돌리기
# 아스키코드값으로 공백 갯수 올리기 +1
    # 첫 idx값이 공백이면 공백갯수대로 올리기 
            # 인터넷 보고나니 이런 생각이 뭔가 그러네...

## 2908

# num1 , num2 = input().split() ## 이상태로 reverse가 안되는건 num1 자체는 str으로 되어서 그런가봄.. # tpye결과는 str이니... 
                        # 테스트 결과 즉 저렇게 list 박는건... 의미가 없다..
# if int(num1[2]+num1[1]+num1[0]) > int(num2[2]+num2[1]+num2[0]):
#     print(num1[2]+num1[1]+num1[0])
# else:
#     print(num2[2]+num2[1]+num2[0])

        # 아 내가 일일이 돌리지 않아도 list를 역전시키는 함수 .reverse가 있다...

## 인터넷 방법..
# a, b = map(reversed,input().split())
#  ## reversed는 반대 방향으로 순회하는 객체를 만듬.
# print(type(a))
# print(a)
# a,b = "".join(a), "".join(b) #join은 객체들을 합침.

# if a >=b:
#     print(a)
# else:
#     print(b)

## 5622

# 받은 문자를 나누기.
# 특정 숫자에 문자 입력 (단 시간 구하는거니, 숫자 1 = 2초니 숫자에 +1 할수 있게하기.)

# 노가다형... 
# test = list(map(str,input()))
# num2 = list(str("ABC"))
# num3 = list(str("DEF"))
# num4 = list(str("GHI"))
# num5 = list(str("JKL"))
# num6 = list(str("MNO"))
# num7 = list(str("PQRS"))
# num8 = list(str("TUV"))
# num9 = list(str("WXYZ"))

# count = 0

# for i in test:
#         for j in range(len(num2)):
#                 if i == num2[j]:
#                         count += 3
#                 elif i == num3[j]:
#                         count += 4
#                 elif i == num4[j]:
#                         count += 5
#                 elif i == num5[j]:
#                         count += 6
#                 elif i == num6[j]:
#                         count += 7
#                 elif i == num8[j]:
#                         count += 9
#         for l in range(len(num7)):
#                 if i == num7[l]:
#                         count += 8
#                 elif i == num9[l]:
#                         count += 10

# print(count)

## 인터넷 방법

# li=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word=input()
# cnt=0
# for i in range(len(word)):
#     for j in li:
#         if word[i] in j:
#             cnt+=li.index(j)+3
# print(cnt)
        ## 저 코드를 줄일 방법 중 '안에 있는가' 여부를 판단하는 함수를 뭔지 모르고 있었음. 노가다로 코드 쓰면서도 방법이 있는데 까먹었다고, 계속 생각.


