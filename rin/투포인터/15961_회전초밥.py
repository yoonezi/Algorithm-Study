'''
시간 제한 1초 
슬라이딩 윈도우 사용
시간복잡도 O(n)
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(n)]
    
arr = defaultdict(int)
arr[c] = 1

# 맨처음 종류 카운트
cnt = 1
for i in range(k):
    if arr[sushis[i]] == 0:
        cnt += 1
    arr[sushis[i]] += 1
    
res = cnt

for end in range(k, n + k - 1):
    # 맨앞 없애기
    arr[sushis[end - k]] -= 1
    if arr[sushis[end - k]] == 0:
        cnt -= 1      
    # 맨끝 추가하기
    arr[sushis[end % n]] += 1
    if arr[sushis[end % n]] == 1:
        cnt += 1   
    res = max(cnt, res) # 종류 최대값 갱신
print(res)
