import heapq
N, M = map(int,input().split())
li = [[] for _ in range(N)]
hq = []
max_val, min_val = 0, 10**10
for i in range(N):
    li[i] = sorted(list(map(int, input().split())))
    max_val = max(max_val, li[i][0])
    min_val = min(min_val, li[i][0])
    heapq.heappush(hq, (li[i][0], i, 0))
res = 10**10

while hq:
    min_val, idx, jdx = heapq.heappop(hq)
    res = min(res, max_val - min_val)
    if jdx + 1 >= M:
        break

    heapq.heappush(hq, (li[idx][jdx+1], idx, jdx+1))
    max_val = max(max_val, li[idx][jdx+1])
print(res)