N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
res = 10**18
for j in range(3):
    dp = [[0 for _ in range(3)] for _ in range(N)]
    dp[0][j] = li[0][j]
    dp[0][j-1] = 1001
    dp[0][(j+1)%3] = 1001
    for i in range(1,N-1):
        for k in range(3):
            dp[i][k] = min(dp[i-1][k-1], dp[i-1][(k+1)%3]) + li[i][k]
    dp[N-1][j-1] = min(dp[N-2][j-2], dp[N-2][j]) + li[N-1][j-1]
    dp[N-1][(j+1)%3] = min(dp[N-2][j], dp[N-2][(j+2)%3]) + li[N-1][(j+1)%3]
    res = min(res, min(dp[N-1][(j+1)%3],dp[N-1][j-1]))
print(res)