N, M = map(int, input().split())
li = list(map(int, input().split()))

def ride_cnt(time):
    cnt = M
    for i in range(M):
        cnt += time // li[i]
    return cnt

def find():
    left = 0
    right = 60_000_000_000
    while left < right:
        mid = (left + right) // 2
        if ride_cnt(mid) >= N:
            right = mid
        else:
            left = mid + 1
    return left

if N <= M:
    print(N)
else:
    time = find()
    cnt = M
    for i in range(M):
        cnt += (time-1) // li[i]
    for i in range(M):
        if time % li[i] == 0:
            cnt += 1
            if cnt == N:
                print(i+1)
                break
