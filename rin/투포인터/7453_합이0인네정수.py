'''
시간제한 12초 == 12억번
n 최대 4000

완탐으로 풀면 O(N^4) -> 시간초과

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()
# print(ab, cd)
i = 0
j = len(cd) - 1

res = 0

while i < len(ab) and j >= 0:
    if ab[i] + cd[j] == 0:
        ni = i + 1 
        nj = j - 1
        while ni < len(ab) and ab[i] == ab[ni]: 
            ni += 1
        while nj >= 0 and cd[j] == cd[nj]: 
            nj -= 1
        
        res += (ni - i) * (j - nj) 
        i = ni
        j = nj

    elif ab[i] + cd[j] > 0:
        j -= 1
    else: 
        i += 1

print(res)