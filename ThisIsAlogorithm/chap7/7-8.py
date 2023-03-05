n,m = map(int,input().split())

tteoks = list(map(int,input().split()))

tteoks.sort()

start = 0
end = max(tteoks)
total = 0
result = 0

while start<=end:
    mid = (start+end)//2
    for i in tteoks:
        if i>mid:
            total += (i-mid)
    if total == m:
        result = mid
        break
    elif total > m:
        start = mid+1
    elif total < m:
        end = mid-1
    total = 0
    
print(result)