import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

lis = []
lis.append(li[0])

def lower_bound(target):
    left = 0
    right = len(lis)-1
    while left < right:
        mid = (left + right) // 2
        if lis[mid] > target:
            right = mid
        else :
            left = mid + 1
    return left

for i in range(1,N):
    if lis[-1] < li[i]:
        # 들어갈 수 있는 경우에는
        lis.append(li[i])
    else:
        # 들어갈 수 없는 경우에는 이분탐색으로 위치 찾아서 넣음
        jdx = lower_bound(li[i])
        lis[jdx] = li[i]
print(N - len(lis))