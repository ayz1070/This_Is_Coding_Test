import heapq

B = [5,7,3,4,1]
arr = list()
for i in B:
    heapq.heappush(arr, i)

print(arr)