'''
[문제]
n가지 종류의 동전이 있다. 
이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
그러면서 "동전의 개수가 최소"가 되도록 하려고 한다. 
각각의 동전은 몇 개라도 사용할 수 있다.

[입력]
(1 ≤ n ≤ 100)

[시간제한]
1초 = O(N^4)


[접근]
1) 문제에서 '가치의 합이 k원이 되는 최소 동전의 수'를 구하라는 문장을
'가치의 합이 i(0<=i<=k)원이 되는 최소 동전의 수'로 작게 나눠 볼 수 있다.
(여기서 먼저 dp 테이블의 형태가 [0]*(k+1) 일 것이라고 유추해 볼 수 있음

2.) 점화식 찾기
dp[i] = min(dp[i - coin]+1, dp[i])
'''

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for coin in arr:
    for i in range(coin, k + 1):  
        dp[i] = min(dp[i - coin] + 1, dp[i])
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])