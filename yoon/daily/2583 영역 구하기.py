m, n, k = map(int, input().split()) #m:x, n:y
arr = [[1 for _ in range(n)] for _ in range(m)]

def color(y1, x1, y2, x2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 0
    
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split()) #0 2 4 4
    color(y1, x1, y2, x2)
    
ans = []

def dfs(x, y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                cnt += 1
                dfs(nx, ny)

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 1
            arr[i][j] = 0
            dfs(i, j)
            ans.append(cnt)
print(len(ans))
ans.sort()
print(*ans)
