n,m,k = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort(reverse=True)

result = 0

for i in range(1,m+1):
    if i % (k+1) !=0:
        result += nums[0]
    else:
        result += nums[1]
    print(result)

print(result)