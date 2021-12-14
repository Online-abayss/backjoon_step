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


n, m = input().split()
cards = list(map(int,input().split()))
sum = []

for i in range(0,int(n)-2):
    for j in range(i+1,int(n)-1):
        for z in range(j+1,int(n)):
                sum.append(cards[i]+cards[j]+cards[z])
a = set(sum)
b = list(a)
sum = b
sum.sort()

for a in range(len(sum)):
    if sum[a]>=int(m):
        if sum[a]-int(m) < int(m)-sum[a-1]:
            print(sum[a-1])
            break
        print(sum[a])
        break          
print(sum)
