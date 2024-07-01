'''
[목표]
✨ 시간 복잡도 생각하면서 문제 풀어보기
파이썬은 1초에 2000만 = 20,000,000 번 연산이 가능
시간제한이 1초, n = 100,000 (10만) 이라고 할 때
O(N^2) 으로 알고리즘을 짜게 되면 10,000,000,000 = 100억 번의 연산이 필요하므로, 시간초과가 나게 된다.
이 경우엔 O(NlogN) 으로 알고리즘을 짜야 1,600,000 번의 연산으로 수행 가능하다. (log 100,000 = 약 16)

[문제]
세준이는 크기가 NxN인 배열 A를 만들었다.
배열에 들어있는 수 A[i][j] = ixj 이다. 
이 수를 일차원 배열 B에 넣으면 B의 크기는 NxN이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.
배열 A와 B의 인덱스는 1부터 시작한다.

[접근]
이 문제는 시간복잡도와 효율성을 고려한 로직을 세워야한다.
문제의 조건을 보면 N은 최대 10^5이고, K는 최대 10^9이다.

O(N^2) 알고리즘으로 풀면, 10^10 연산을 수행해야한다.
-> 시간초과
따라서 배열을 직접 생성하는 과정은 O(N^2)이기 때문에 다른 방법을 찾아야 한다.

O(NlongN) 알고리즘으로 풀면,
100,000 * 16 = 1,600,000번의 연산
> 약 0.016초 걸린다.

✔️  따라서 이 문제는 O(NlogN) 알고리즘으로 풀어야한다.
✨ 파라메트릭 서치
'''

n = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in range(1, n+1):
        tmp += min(mid//i, n)

    if tmp >= k:
        ans = mid
        end = mid - 1
        
    else:
        start = mid + 1
        
print(ans)