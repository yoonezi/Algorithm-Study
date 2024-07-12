from itertools import combinations as cb
import sys
input = sys.stdin.readline

N = int(input())
li = [i for i in range(N)]
grid = [list(map(int, input().split())) for _ in range(N)]
res = 10**18

for i in range(1, N//2+1):
    comb = list(cb(li,i))
    for a_team in comb:
        b_team = tuple(set(li) - set(a_team))
        a_sum, b_sum = 0, 0
        for i, j in cb(a_team, 2):
            a_sum += grid[i][j] + grid[j][i]
        for i, j in cb(b_team,2):
            b_sum += grid[i][j] + grid[j][i]
        res = min(res, abs(a_sum - b_sum))
print(res)