import sys
input = sys.stdin.readline

N, C = map(int, input().split())
li = []
ans = N - 1

for _ in range(N):
    li.append(int(input()))
li.sort()
def can_go(dist):
    cnt = C-1
    prev = 0
    for i in range(1, N):
        if li[i] - li[prev] >= dist:
            prev = i
            cnt -= 1
            if cnt == 0:
                return True
    return False

def ps():
    global ans
    left = 0
    right = 10**18
    while left <= right:
        mid = (left + right) // 2
        if can_go(mid):
            ans = mid
            left = mid + 1
        else :
            right = mid - 1
ps()
print(ans)