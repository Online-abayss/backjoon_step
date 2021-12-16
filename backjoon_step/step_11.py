#2798

# 1,2,3
# 1,2,4
# 1,2,5
# 1,3,4
# 1,3,5
# 1,4,5
# 2,3,4
# 2,3,5
# 2,4,5
# 3,4,5


# for i in range(0,n-2):
#     for j in range(i+1,n-1):
#         for z in range(j+1,n):
#             각 자리수 더하기
# 각 자릿수 리스트 형식으로 저장 후 높은 순으로 정리. 
# 높은 수로 정리한걸 for문으로 비교하여 같거나 작으면 그 값을 출력.
     # 이리하니 500 기준 504짜리가 나오는걸 보니 뺼때 절대값을 이용하여 해야할듯.
# 시간초과될듯 ㅎ...
# 흐... 인덱스로 해서 순서랑 이용하던거 배웟는데 까먹었다. 그거 하면 더 쉽게 할거같은데.
# enumerate 이거엿던같음.
# 인터넷 보기 전의 나의 머리속에서 최대치인듯.


# n, m = input().split()
# cards = list(map(int,input().split()))
# sum = []

# for i in range(0,int(n)-2):
#     for j in range(i+1,int(n)-1):
#         for z in range(j+1,int(n)):
#                 sum.append(cards[i]+cards[j]+cards[z])
# a1 = set(sum)
# b = list(a1)
# sum = b
# sum.sort()

# for a in range(len(sum)):
#     if sum[a]>=int(m):
#         if sum[a]-int(m) < int(m)-sum[a-1]:
#             print(sum[a-1])
#             break
#         print(sum[a])
#         break
    
# print(a)
# print(sum[a-1])
# print(sum)
# 위에는 인터넷 안보고 내 스스로 풀려 했으나 가장 가까운 수를 정하는 방식을 제대로 표현 못하여 실패... 2시간 넘게 고민했는데...
# 인터넷 보고 감탄.

# n, m = map(int,input().split())
# cards = list(map(int,input().split()))
# result = 0
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             sum = cards[i]+cards[j]+cards[k]
#             if sum <= m:
#                 result = max(sum, result)
# print(result)

# 내꺼랑 인터넷꺼의 비교점. 1. 내가 2시간동안 머리 싸매고 길게 쓴 코드가 결국엔 단순한 max의 함수 사용...
# 2. 내껀 리스트에 저장하여 그 모든걸 구한 다음, 중복값을 삭제하여 나열 한뒤에 비교하는거지만, 이건 실시간으로 그때 비교하여 구함.
# 결론 . 잘 알아두고... 머리가 유연해지기...
# 글구 모듈 불러와서 함수 사용하는 법들도 있지만. 일단 한바퀴 돌기전에 최대한 사용하지 않을 예정

#2231

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
## list만 [1.... ] 있다고 생각하지말자. str도 가능하다. 너무 어렵게 생각하지말자.


#7568
weight = 55
height = 185

