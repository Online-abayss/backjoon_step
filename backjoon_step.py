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