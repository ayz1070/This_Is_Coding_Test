n = int(input())

coins = [500,100,50,10]
count = 0

for i in coins:
    count += n//i
    n = n%i
    print(count,n)

print(count)        