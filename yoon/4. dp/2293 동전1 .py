'''
[문제]
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오.

"각각의 동전은 몇 개라도 사용할 수 있다."
"사용한 동전의 구성이 같은데, 순서만 다른 것"은 "같은 경우"이다.

[입력]
(1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)

[시간제한]
0.5초 = N^4

[시간복잡도]
O(N^2)

[접근]
1) 문제에서 '가치의 합이 k원이 되는 경우의 수'를 구하라는 문장을
'가치의 합이 i(0<=i<=k)원이 되는 경우의 수'로 작게 나눠 볼 수 있다.
(여기서 먼저 dp 테이블의 형태가 [0]*(k+1) 일 것이라고 유추해 볼 수 있음

2.) 점화식 찾기
dp[i] = dp[i] + dp[i - coin]

https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-2293%EB%B2%88-%EB%8F%99%EC%A0%84-1-python-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D

'''


n, k = map(int, input().strip().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for coin in arr:
    for i in range(coin, k + 1):  
        dp[i] += dp[i - coin]
        # print(dp)

print(dp[k])