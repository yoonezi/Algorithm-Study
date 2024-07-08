'''
[문제]
1. 원래 회전 초밥은 손님이 마음대로 초밥을  고르고, 먹은 초밥만큼 식대를 계산하지만, 
벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다. 

2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고,
1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다.
만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공한다.  

[접근]
일단 원형이니 배열 두배
k개 접시 연속 : 슬라이딩 윈도우
로 풀면 될 거 같다.

[시간 복잡도]
O(n)
'''
from collections import defaultdict
n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
sushi = sushi + sushi

start = 0
end = 0
dic = defaultdict(int)
ans = 0

dic[c] += 1

while end < k:
    dic[sushi[end]] += 1
    end += 1

while end < len(sushi):
    ans = max(ans, len(dic))
    
    dic[sushi[start]] -= 1
    if dic[sushi[start]] == 0:
        del dic[sushi[start]]
                
    dic[sushi[end]] += 1
    start += 1
    end += 1
    
print(ans)