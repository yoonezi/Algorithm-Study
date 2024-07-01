'''
[문제]
공화국에 있는 유스타운 시에서는 길을 사이에 두고 전봇대가 아래와 같이 두 줄로 늘어서 있다.
그리고 길 왼편과 길 오른편의 전봇대는 하나의 전선으로 연결되어 있다.
어떤 전봇대도 두 개 이상의 다른 전봇대와 연결되어 있지는 않다.

문제는 이 두 전봇대 사이에 있는 전깃줄이 매우 꼬여 있다는 점이다
꼬여있는 전깃줄은 화재를 유발할 가능성이 있기 때문에 유스타운 시의 시장 임한수는 전격적으로 이 문제를 해결하기로 했다.

임한수는 꼬여 있는 전깃줄 중 몇 개를 적절히 잘라 내어 이 문제를 해결하기로 했다.
하지만 이미 설치해 놓은 전선이 아깝기 때문에 "잘라내는 전선을 최소로 하여" 꼬여 있는 전선이 하나도 없게 만들려고 한다.

유스타운 시의 시장 임한수를 도와 "잘라내야 할 전선의 최소 개수"를 구하는 프로그램을 작성하시오.

[접근]
두 전봇대는 오름차순으로 정렬
문제의 핵심은 LIS의 길이를 물어보고 있다는 점
LIS가 엉망이어도 상관이 없다.

[시간복잡도]
n 은 10^5이기 때문에 O(n^2)으로는 풀면 안됨
따라서 O(NlogN)으로 풀어야함
이런 문제는 LIS유형같아서 .. 이걸로 해보겠습니다
'''

n = int(input())
lines = list(map(int, input().split()))
'''
res = [lines[0]]

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end)//2
        if res[mid] ==  target:
            return mid
        elif res[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
    return start

for i in range(1, n):
    if res[-1] < lines[i]:
        res.append(lines[i])
    else:
        idx = binary_search(0, len(res)-1, lines[i])
        res[idx] = lines[i]
print(n - len(res))
'''
# ''' bisect_left 적용ver
from bisect import bisect_left

res = [lines[0]]
for i in range(1, n):
    if res[-1] < lines[i]:
        res.append(lines[i])
    else:
        idx = bisect_left(res, lines[i])
        res[idx] = lines[i]
print(n - len(res))
# '''