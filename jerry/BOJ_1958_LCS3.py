import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()

# 파이썬 문법 ... 곱하기를 통한 배열 증식은 얉은 복사를 기본으로 하고 있으므로,
# 빠르다는 이유로 곱 연산을 통한 배열 증식을 사용하려 할 때에는 다중 차원 배열이라면
# 최 하단의 리스트만 곱연산으로 하는 것을 권장 (안그럼 값 변경이 의도치않게 발생 가능)
dp = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        for k in range(1, len(c) + 1):
            if a[i-1] == b[j-1] == c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(a)][len(b)][len(c)])