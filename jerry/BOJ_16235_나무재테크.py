from collections import deque
import sys
input = sys.stdin.readline

# 시간복잡도 : O(N^2 * M * K) -> 792 ms

N, M, K = map(int, input().split()) # N 땅 크기, M 나무 개수, k 년 수
grid = [[5 for _ in range(N)] for _ in range(N)] # 기본 영양분 맵
bonus = [[] for _ in range(N)] # 추가 영양분 맵
tree = [[[] for _ in range(N)] for _ in range(N)] # 나무 정보 - 3차원 리스트
dead = deque()
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(N):
    bonus[i] = list(map(int, input().split()))
for i in range(M):
    y, x, z = map(int, input().split())
    tree[y-1][x-1].append(z)

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def spring():
    for y in range(N):
        for x in range(N):
            alive = []
            now_tree = sorted(tree[y][x])
            for z in now_tree:
                if grid[y][x] >= z:
                    alive.append(z+1)
                    grid[y][x] -= z
                else:
                    dead.append([y, x, z])
            tree[y][x] = alive.copy()
def summer():
    while dead:
        y, x, z = dead.pop()
        grid[y][x] += z // 2
def fall():
    for y in range(N):
        for x in range(N):
            for z in tree[y][x]:
                if z % 5 == 0:
                    for i in range(8):
                        if in_range(y + dy[i], x + dx[i]):
                            tree[y+dy[i]][x+dx[i]].append(1)
def winter():
    for y in range(N):
        for x in range(N):
            grid[y][x] += bonus[y][x]
    return

def simulation():
    spring()
    summer()
    fall()
    winter()

def get_answer():
    ans = 0
    for y in range(N):
        for x in range(N):
            ans += len(tree[y][x])
    return ans

for _ in range(K):
    simulation()
print(get_answer())