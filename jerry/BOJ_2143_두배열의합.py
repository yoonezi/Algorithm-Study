import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
brr = list(map(int, input().split()))

"""
단순하게 하면 O(N^2 * M^2) : 모든 경우의 수 브루트포스
각각 N*logN으로 줄일 순 없을까? -> 누적합 ; 가능할 듯
"""

psa = [0]
for i in range(0,N):
    psa.append(psa[-1] + arr[i])
psb = [0]
for i in range(0, M):
    psb.append(psb[-1] + brr[i])

a_dict = defaultdict(int)
b_dict = defaultdict(int)

for i in range(1, N+1): # subarray 길이
    for j in range(0, N - i + 1):
        ps = psa[j+i] - psa[j]
        a_dict[ps] = a_dict[ps] + 1
for i in range(1, M+1):
    for j in range(0, M - i + 1):
        ps = psb[j+i] - psb[j]
        b_dict[ps] = b_dict[ps] + 1
a_keys = sorted(a_dict.keys())
b_keys = sorted(b_dict.keys())

def bs(v):
    left = 0
    right = len(b_keys) - 1
    while left <= right:
        mid = (left + right) // 2
        if b_keys[mid] + v == T:
            return b_dict[b_keys[mid]]
        elif b_keys[mid] + v < T:
            left = mid + 1
        else :
            right = mid - 1
    return 0

ans = 0
for i in a_keys:
    ans += (bs(i) * a_dict[i])
print(ans)