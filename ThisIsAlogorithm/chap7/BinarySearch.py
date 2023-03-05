def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid = (start + end)//2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr,target,start,mid-1)
    elif target > arr[mid]:
        return binary_search(arr,target,mid+1,end)

arr = [1,3,5,7,9,11,13,15,17]

print(binary_search(arr,13,0,len(arr)-1))

