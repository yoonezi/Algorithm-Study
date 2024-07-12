import sys
from itertools import combinations as cb

input = sys.stdin.readline

N, C = map(int, input().split())
li = list(map(int, input().split()))

arr = li[:len(li) // 2]
brr = li[len(li) // 2:]

acb = [0]
bcb = [0]

for i in range(1, len(arr)+1):
    for sub in cb(arr, i):
        acb.append(sum(sub))
for i in range(1, len(brr)+1):
    for sub in cb(brr, i):
        bcb.append(sum(sub))

def upper_bound(target):
    bcb.sort()
    left = 0
    right = len(bcb) - 1
    while left < right:
        mid = (left + right) // 2
        if bcb[mid] + target > C:
            right = mid
        else:
            left = mid + 1
    return left

res = 0
for i in acb:
    if i + bcb[upper_bound(i)] <= C:
        res += upper_bound(i) + 1
    else:
        res += upper_bound(i)
print(res)

