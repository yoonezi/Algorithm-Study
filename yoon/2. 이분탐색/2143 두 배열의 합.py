'''
[문제]
한 배열 A[1], A[2], …, A[n]에 대해서, 
부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다.  

이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 
각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때, 
A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우,
부 배열 쌍의 개수는 다음의 7가지 경우가 있다.

T(=5) = A[1] + B[1] + B[2]
      = A[1] + A[2] + B[1]
      = A[2] + B[3]
      = A[2] + A[3] + B[1]
      = A[3] + B[1] + B[2]
      = A[3] + A[4] + B[3]
      = A[4] + B[2] 
      
[접근]
배열이 두개인데 어떻게 범위 설정?
..
누적합 + 이분탐색
'''

import bisect


t = int(input())

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

asum = []
bsum = []

for i in range(n):
    for j in range(n):
        asum.append(sum(arr[i:j]))

for i in range(n):
    for j in range(n):
        bsum.append(sum(brr[i:j]))

asum.sort()
bsum.sort()

ans = 0
for i in range(len(asum)):
    left = bisect.bisect_left(bsum,t - asum[i])
    right = bisect.bisect_right(bsum,t -asum[i])
    ans += left - right
    
print(ans)
