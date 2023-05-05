# L R U D
dx = [0,0,-1,1]
dy = [-1,1,0,0]

directions = ['L','R','U','D']
# 시작점
x,y=1,1

plans = input().split()

for plan in plans:
    
    for i in range(len(directions)):
        if plan == directions[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 0 or ny <0 or nx>n or xy>
