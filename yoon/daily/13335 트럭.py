'''
[문제]
강을 가로지르는 하나의 차선으로 된 다리가 하나 있다.
이 다리를 n 개의 트럭이 건너가려고 한다. 
트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다. 
다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다. 
다리의 길이는 w 단위길이(unit distance)이며, 
각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 
동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다. 
참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.

예를 들어, 다리의 길이 w는 2, 다리의 최대하중 L은 10, 
다리를 건너려는 트럭이 트럭의 무게가 [7, 4, 5, 6]인 순서대로 다리를 오른쪽에서 왼쪽으로 건넌다고 하자. 
이 경우 모든 트럭이 다리를 건너는 최단시간은 아래의 그림에서 보는 것과 같이 8 이다.

[입력]
시간 제한 : 1초
n (1 ≤ n ≤ 1,000) 
O(N^2) = (10*3)^2 > OK
'''

n, w, l = map(int, input().split())
q = list(map(int, input().split()))

b = [0] * w
time = 0
while b:
	time += 1
	b.pop(0) 
	if q:
		if sum(b) + q[0] <= l:
			b.append(q.pop(0))
		else:
			b.append(0) 
print(time)

# bridge = deque()
# while queue or bridge:
#     time += 1
    
#     if bridge:
#         if time - bridge[0][1] >= w:
#             bridge.popleft()
    
#     if queue:
#         if sum(truck[0] for truck in bridge) + queue[0] <= l and len(bridge) < w:
#             truck_weight = queue.popleft()
#             bridge.append((truck_weight, time))
            
# print(time)

