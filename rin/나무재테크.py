N,M,K = map(int, input().split())
A = [
    list(map(int, input().split()))
    for _ in range(N)
]
ground = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)] 

#첫나무심기
for _ in range(M):
    r,c, age = map(int, input().split())
    tree[r-1][c-1].append(age)



#봄-여름
def spring_summer():
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                live = []
                dead = []
                for t in tree[i][j]:
                    if ground[i][j] >= t:
                        ground[i][j] -= t
                        live.append(t + 1)
                    else:
                        dead.append(t)
                tree[i][j] = live
                for t in dead:
                    ground[i][j] += t//2
                        
                    
#가을
# 나무 나이 5의 배수인애를 가지고 있는 애 찾고
# 걔랑 인접한 8칸에 1살나이 나무 다 append

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def fall():
    for i in range(N):
        for j in range(N):
            if tree[i][j]: 
                for k in tree[i][j]:
                    if k % 5 == 0:
                        for l in range(8):
                            nx, ny = i + dx[l], j + dy[l]
                            if 0 <= nx < N and 0 <= ny < N:
                                tree[nx][ny].append(1)
                    
#겨울
def winter():
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]

for _ in range(K):
    spring_summer()
    fall()
    winter()

answer = 0
#출력
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])


print(answer)