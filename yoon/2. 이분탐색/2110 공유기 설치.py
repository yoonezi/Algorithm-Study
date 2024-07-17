'''
<문제>
집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 
한 집에는 공유기를 하나만 설치할 수 있고, 
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 
가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

<접근>
1. 일단 집 sort
2. 공유기 거리를 이진탐색

<시간 복잡도>
이진탐색 : O(logN)

'''
n, k = map(int, input().split())
wifi = []
for _ in range(n):
    wifi.append(int(input()))    
wifi.sort()

start = 1
# end = max(wifi) - min(wifi)
end = wifi[-1] - wifi[0]

ans = 0

while start <= end:
    mid = (start + end) // 2
    now = wifi[0]
    cnt = 1
    
    for i in range(1, len(wifi)):
        if wifi[i] >= now + mid:
            cnt += 1
            now = wifi[i]
        
    if cnt >= k:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
        
print(ans)
    
