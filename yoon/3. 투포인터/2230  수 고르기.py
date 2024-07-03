'''
[문제]
N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다.
이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다),
그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.

예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자.
만약 M = 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 
이 중에서 차이가 가장 작은 경우는 1 4나 2 5를 골랐을 때의 3이 된다.

[입력]
1 ≤ N ≤ 100,000

만약 완탐으로 풀면, O(N^2) == (10^5)^2
즉, 2초 이상으로 시간초과

O(nlogn), O(n^2logn) ok

[반례]
4 3
10
2
10
8
ans : 6

✨[Reivew]
처음에는 
start = 0
end = n - 1 이렇게 두고 풀었는데, 다른 반례에서 통과가 안됐다.
이래저래 반례두고 풀어도 안되는게 많다..

이유가 뭘까?
이렇게 풀면, "모든 경우의 수를 고려하지 않고 일부 경우를 놓칠 수 있기 때문"이다..

문제에서는 배열에서 두 수를 선택했을 때 그 차이가 M 이상이면서 최소인 경우를 찾는 것이므로,
정렬된 상태에서 두 포인터를 이용해 모든 경우를 탐색하면서 최소 차이를 찾아나가는 방식이 적절하다

'''

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()

start, end = 0, 0
min_val = 2000000001

falg = False
while start < n and end < n:
    s = arr[end] - arr[start]
    if s < m:
        end += 1
    elif s > m:
        min_val = min(s, min_val)
        start += 1
    else:
        falg = True
        break
if falg:
    print(m)
else:
    print(min_val)