import sys
input = sys.stdin.readline


#예전에 풀어봤던 문제 같다. 이 문제 핵심 해결법을 이미 알고있어서..
#근데 예전엔 결국 스스로 못 풀었었으니까..
#핵심 해결법을 이미 알지만? 그래도 스스로 생각을 가지고 구현해봤음
N, C = map(int, input().split())
house = []
for i in range(N):
    a = int(input())
    house.append(a)
house.sort()

s = 1
e = house[-1] - house[0]
answer = 0

while s <= e:
    m = (s + e) // 2
    cur = house[0]
    cnt = 1
    for i in range(1,N):
        if house[i] >= cur + m:
            cnt += 1
            cur = house[i]
    if cnt >= C:
        s = m + 1
        answer = m
    else:
        e = m - 1

print(answer)
