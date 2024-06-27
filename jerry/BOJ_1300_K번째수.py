import sys
input = sys.stdin.readline

N = int(input())
K = int(input()) - 1

def cal(t):
    res = 0
    for i in range(1, N+1):
        if t // i <= N:
            res += t // i
        else :
            res += N
    return res

def lower_bound():
    left = 1
    right = 10**18
    while left < right:
        mid = (left + right) // 2
        if cal(mid) > K:
            right = mid
        else:
            left = mid + 1
    return left

print(lower_bound())