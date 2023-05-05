from collections import deque

n = int(input())

area = 0
color_blind_area = 0
graph = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
# 큐 생성
queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# bfs
def bfs(x,y):
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                    # 방문 처리
                    visited[nx][ny] = True
                    queue.append((nx,ny))

# 적록 색맹이 아닌 경우 바로 bfs 수행
for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            area += 1
            bfs(x,y)

# 적록 색맹인 경우 G를 R로 치환
for x in range(n):
    for y in range(n):
        if graph[x][y] == 'G':
            graph[x][y] = 'R'

visited = [[False]*n for _ in range(n)]

# G를 R로 치환하고 bfs 수행하면 적록 생맹의 경우 구역 개수
for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            color_blind_area += 1
            bfs(x,y)
            
print(area, color_blind_area)