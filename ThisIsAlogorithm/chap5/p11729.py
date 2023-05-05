# count = 0

# def Hanoi(num,start,mid,end):
#     global count 
#     if num == 1:
#         print(f"{start} {end}")
#         count +=1
#     else:
#         Hanoi(num-1,start,end,mid)
#         count +=1
#         print(f"{start} {end}")
#         Hanoi(num-1,mid,start,end)    
    

# n = int(input())
# print(count)
# Hanoi(n,1,2,3)

count = 0
result = []
def Hanoi(num,start,mid,end):
    global count 
    if num == 1:
        print(f"{start} {end}")
        count +=1
    else:
        Hanoi(num-1,start,end,mid)
        count +=1
        print(f"{start} {end}")
        Hanoi(num-1,mid,start,end)
    
    

n = int(input())
print(2**n-1)
Hanoi(n,1,2,3)
