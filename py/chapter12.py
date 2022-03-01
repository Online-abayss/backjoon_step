## 2750

# case = int(input())

# num_list = []
# for i in range(case):
#     num_list.append(int(input()))
#     num_list.sort()
# for j in range(len(num_list)):
#     print(num_list[j])

## 2751
# import sys
# num = sys.stdin.readline
# test= []
# for i in range(int(num())):
#     test.append(int(num()))
# test= sorted(test)
# for i in test:
#     print(i)

## 10989

# import sys
# num = sys.stdin.readline
# num_list = [0] * 10001
# for _ in range(int(num())):
#     temp = int(num())
#     num_list[temp] += 1
# for i in range(10001):
#     if num_list[i] != 0:
#         for j in range(num_list[i]):
#             print(i)

## 2108

# 1. sum(n) / n  , 2. n들을 오름차순 시 가운뎃값 3. n들 중 빈도수가 많은 수 4. n들 중 최솟값과 최댓값의 차이.











## 1427

# num =list(map(int,input()))
# num.sort(reverse=True)
# for i in num:
#     print(i,end="")

## 11650

 # 정답 갈려다 만 실패작.

# case = int(input())
# num_list = []
# for _ in range(case):
#     x,y = map(int,input().split())
#     num_list.append((x,y))
# num_list.sort()

# 정답.

# case = int(input())
# num_list = [list(map(int,input().split())) for i in range(case)]

# num_list.sort()

# for i in num_list:
#     for j in i:
#         print(j, end= " ")
#     print("")

## 인터넷 보고 정답 개량형. #하지만 여전히 느리다.
# case = int(input())
# num_list = [list(map(int,input().split())) for i in range(case)]

# num_list.sort()

# for i,j in num_list:
#     print(i, j)

## 인터넷 정답. // 확실히 input()과 sys의 차이는 큰거같다.

# import sys                           # sys.stdin.readline을 사용하기 위해
# input = sys.stdin.readline           # 속도향상을 위해 inputr()대신 readline사용

# test_case = int(input())             # 테스트 케이스 입력받기

# list_to_sort = []                    # 정렬할 좌표를 담을 리스트 선언
# for _ in range(test_case):                # 테스트 케이스만큼 입력받기
#     x, y = map(int, input().split())      # x, y로 나눠 입력받기
#     list_to_sort.append((x, y))           # (x, y)튜플의 형태로 리스트에 담기 

# for i, j in sorted(list_to_sort):         # 리스트에 담긴 좌표를 정렬하기
#     print(i, j)            


## 11651
import sys

input = sys.stdin.readline
case = int(input())
num_list = [list(map(int,input().split())) for i in range(case)]

num_list.sort()

for i,j in num_list:
    print(i, j)


