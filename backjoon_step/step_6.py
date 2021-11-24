# 15596

# def solve(a):
#     ans = sum(a)
#     return ans

# 4673


def d(n):
    sum = 0
    count = []
    for i in range(len(str(n))):
        sum += n//(10**i)
        
    sum += n%(10**i)

    if n == sum:
        count = n

    return(count)

for i in range(1,30):
    print(d(i))


         
# for i in range(10,20):

