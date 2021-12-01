#1712

a,b,price = map(int,input().split())

count = 0
while(True):
    if ((a * count) + (b * count)) < (price *count):
        break
    count += 1
print(count)