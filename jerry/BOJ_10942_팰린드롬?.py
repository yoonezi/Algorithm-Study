import sys
input = sys.stdin.readline

# time complexity : O(N^2)
N = int(input())
li = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if li[i] == li[i+1]: dp[i][i+1] = 1
for l in range(N-2):
    for i in range(N-2-l):
        j = i + 2 + l
        if li[i] == li[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])