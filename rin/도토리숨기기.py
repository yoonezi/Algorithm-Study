'''
N : 상자수
K : 규칙수 (줄)
D : 도토리 개수
'''
import sys
input = sys.stdin.readline

N,K,D = map(int, input().split())
#먼소리지?
rules = [
    list(map(int, input().split()))
    for _ in range(K)
]

# 상자 개수를 기준으로 이분탐색 시작
# target이 125가 됐다고 하자.
# 125 - a (100) / c (10) = 2
# 125 - a (110) / c (15) = 1
# a를 포함해줘야하니 + 1
# 만일 도토리가 d보다 더 담기면 end를 좁히고
# 덜 담기면 start를 크게

def put(mid):
    res = 0
    for A,B,C in rules:
        if mid < A:
            continue
        B = min(B, mid)
        res += (B - A) // C + 1
    if res >= D:
        return True
    else:
        return False


def search():
    s = 0
    e = N
    while s < e:
        m = (s + e)//2
        if put(m):
            e = m
        else:
            s = m + 1
    return e

print(search())