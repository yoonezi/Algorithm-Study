'''
매 라운드가 시작할 때, 현우는 창영이에게 "100보다 작은 두 숫자 A와 B"를 말해준다.
그러고 난 뒤, 창영이는 다음과 같은 문제를 풀어야 한다.

지금까지 현우가 말한 모든 A와 모든 B를 짝짓는다. 
이때, 각 쌍의 합 중에서 가장 큰 값을 작게 만들어라.

즉, 현재 라운드가 N 라운드이라고 하면,
현우가 창영이에게 말한 숫자는 a1, a2, ..., an 과 b1, b2, ..., bn이라고 할 수 있다.

이때, 각 숫자를 한 번씩 사용하여 (ai, bj)쌍을 n개 만들 수 있다.
이렇게 쌍을 모두 만들었을 때, ai+bj의 합 중 가장 큰 값을 가능한 작게 만들어야 한다.

[입력]
제한 : (1 ≤ N ≤ 100000) 
즉 O(N^2) 으로 풀면 (10^5)^2 이므로 시간초과 발생

O(N)이나 O(NlogN)으로 풀어야 하는데..

가장 큰 값이 작은 값이 되도록 만든다..??


'''

n = int(input())
A = []
B = []
ans = 201

# def pointer():
#     start = 0
#     end = 0
#     while start < end:
#         s = 
#     return

def compare():
    return min(min(A)+max(B), max(A)+min(B))

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    print(compare())
    
    # pointer()
    
    
