arr = [3,5,4,1,2]

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
        else:
            break
    print(arr)

print(arr)