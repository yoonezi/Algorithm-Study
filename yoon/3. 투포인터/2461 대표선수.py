'''
# deque([[12, 16, 43, 67], [7, 17, 48, 68], [14, 15, 54, 77]])
# 일단, 다 [0]을 넣어두고, 여기서 최대-최소 값 저장하고 비교하면서 제일 작은 배열의 인덱스 +1 하믄 될듯?

# [시간 복잡도]
# O(N^2)? =  10^6 -> 2초 될 거 같은데 

'''

n, m = map(int, input().split())
arr = []
cur_arr = []

for _ in range(n):
    lst = list(map(int, input().split()))
    lst.sort()
    arr.append(lst)
    cur_arr.append(lst[0])

indices = [0] * n

min_diff = float('inf')

while True:
    min_val = min(cur_arr)
    max_val = max(cur_arr)
    
    min_diff = min(min_diff, max_val - min_val)
    
    min_idx = cur_arr.index(min_val)
    
    indices[min_idx] += 1
    
    if indices[min_idx] == m:
        break
    
    cur_arr[min_idx] = arr[min_idx][indices[min_idx]]

print(min_diff)
