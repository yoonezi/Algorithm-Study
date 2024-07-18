'''
[문제]
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토의 인접한 곳은 "왼쪽, 오른쪽, 앞, 뒤" 네 방향에 있는 토마토를 의미한다.

대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

[입력]
2 ≤ M,N ≤ 1,000 이다

[시간제한]
1초 = 
'''
from collections import deque

n, m = map(int, input().split())
tomatoes = []
for _ in range(m):
    tomatoes.append(list(map(int, input().split())))

mature = deque()
for i in range(m):
    for j in range(n):
        if tomatoes[i][j] == 1:
            mature.append((i,j))

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while mature:
        x, y = mature.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = tomatoes[x][y] + 1
                    mature.append((nx, ny))

bfs()

ans = 0
for i in range(m):
    for j in range(n):
        if tomatoes[i][j] == 0:
            print(-1)
            exit(0)
        else:
            ans = max(ans, tomatoes[i][j])
        
print(ans-1)