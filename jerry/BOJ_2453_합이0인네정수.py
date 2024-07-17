import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
arr = []
brr = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    arr.append((a,b))
    brr.append((c,d))

left_dict = defaultdict(int)
for i in range(N):
    for j in range(N):
        left_dict[arr[i][0] + arr[j][1]] += 1

res = 0
for i in range(N):
    for j in range(N):
        temp = (brr[i][0] + brr[j][1]) * -1
        if temp in left_dict.keys():
            res += left_dict[temp]
print(res)