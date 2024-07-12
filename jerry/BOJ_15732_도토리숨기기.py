import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
li = [[0, 0, 0] for _ in range(K)]


def can_go(box_num):
    res = 0
    for a, b, c in li:
        if box_num >= a:
            if box_num > b:
                res += ((b - a) // c) + 1
            else:
                res += ((box_num - a) // c) + 1
    return res

def bs():
    left = 1
    right = 1_000_000
    while left < right:
        mid = (left + right) // 2
        if can_go(mid) >= D:
            right = mid
        else:
            left = mid + 1
    return left

for i in range(K):
    li[i][0], li[i][1], li[i][2] = map(int, input().split())

ans = bs()
print(ans)