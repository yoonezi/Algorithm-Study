'''
시간제한 2초 == 2억번 연산 가능

n개의 정수로 된 수열 (중복가능)
차이가 m이상 and 최소

n의 최대 100,000

만일 완탐으로 한다하면, O(n^2) 백억번 -> 시간초과

'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

s = 0
e = 0

res =  2,000,000,000

arr.sort()

while s < n and e < n: # 리스트의 길이보다 작아야함
    if arr[e] - arr[s] < m: # m보다 작으면 end를 키움
        e += 1
    else: # m보다 크거나 같을경우 최소값으로 정답 갱신하고 start 키움
        res = min(res,arr[e]-arr[s]) 
        s += 1 

print(res)


'''
정렬 O(nlogn)
투포인터 O(n)
따라서 O(nlogn)으로 풀 수 있음

'''

