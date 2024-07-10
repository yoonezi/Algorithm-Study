import sys 
import heapq

input = sys.stdin.readline


n,m = map(int, input().split())

students = []
for i in range(n):
    students.append(list(map(int, input().split())))

for i in range(n):
    students[i].sort()

heap = []
cur_max = float('-inf')

for i in range(n):
    heapq.heappush(heap, (students[i][0], i, 0))
    cur_max = max(cur_max, students[i][0])

min_diff = float('inf')

while True:
    
    cur_min, row, idx = heapq.heappop(heap)
    min_diff = min(min_diff, cur_max - cur_min)
    
    if idx + 1 < m:
        next = students[row][idx + 1]
        heapq.heappush(heap, (next, row, idx + 1))
        cur_max = max(cur_max, next)
    else:
        break

print(min_diff)

