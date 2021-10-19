#1000
# num1,num2 = input().split()
# print(int(num1+num2)) # 백준 1000번 문제에서 이게 안되는 이유는 
# 일단 결과값이 12로 나오는걸로 보아. 저렇게 하면 사칙연산의 +가 아닌 문자와 문자의 이어주는 형식의 +로 받아드려서 이다.
# 한마디로  int로 묶어서 각각 더하지 않으면 먼저 num1,num2가 문자형으로 받아들여서 합쳐진거.

#1000 문제점의 나만의 해결책 
# num1,num2 = input().split() 
# print(int(num1)/int(num2))

# num1,num2 = map(int,input().split()) 
# print(num1+num2)

# map(적용시킬 함수, 적용할 값들) / 참고 blockmask.tistory.com/531

#10869
# num1,num2 = input().split() 
# print(int(num1)+int(num2))
# print(int(num1)-int(num2))
# print(int(num1)*int(num2))
# print(int(int(num1)/int(num2))) # 앞에 int로 안묶고 그냥 //로 처리해도 된다. //는 나머지가 나와도 몫만 반환하는 연산자
# print(int(num1)%int(num2))

# print("--- 조금 깔끔한 버전---")
# num1,num2 = input().split()
# num1 = int(num1)
# num2 = int(num2)
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1//num2)
# print(num1%num2)

# print("---- 인터넷보고 더 깔끔한버전----" ) # map 써서 하면 2줄코드 됨. 
# print(num1+num2,num1-num2,num1*num2,num1//num2,num1%num2,sep="\n")

#10430

# A,B,C = map(int,input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)


#2588

# a= int(input())
# b= input()
# b0 = b[0]
# b1 = b[1]
# b2 = b[2]

# b0,b1,b2 = map(int,(b0,b1,b2))

# a = "472"
# b = "385"
# -- 제출한 부분 -- 
# 밑에 쉬운 방법도 있었지만 이렇게 한 이유: 뭔가 ... 반복문으로 하면 더 쉬울줄 알아서...
# a= input()
# b= input()

# c = []
# for i in range(len(b)):
#     for j in reversed(range(len(b))):
#         c.append(int(a)*int(b[j]))
#     print(c[i])
# print(int(a)*int(b))
#-- 정말 간단한 식 --
# a = int(input())
# b = input()
# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))

