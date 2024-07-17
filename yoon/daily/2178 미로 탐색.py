from collections import deque

n, m  = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

queue = deque()
queue.append((0,0))

while queue:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
print(arr[n-1][m-1])
                
            