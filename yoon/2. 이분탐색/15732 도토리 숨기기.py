'''
 A번 상자부터 B번 상자까지 C개 간격으로 도토리를 하나씩 더 넣는 규칙을 만들었다! 
 이러한 규칙들을 K개를 만들어
 
 예를 들어 100번 상자부터 150번상자까지 10개 간격으로,
 110번 상자부터 150번 상자까지 15개 간격으로 넣는다면
 100, 110, 120, 125, 130, 140, 150번 상자에 도토리가 있으며
 110번 상자와 140번 상자에는 2개의 도토리가 들어가 있게 된다.
 상자 하나에 들어갈 수 있는 도토리의 개수는 제한이 없으며 앞의 
 상자부터 최대한 꽉꽉 채워나간다고 했을 때 
 마지막 도토리가 들어가 있는 상자의 번호를 출력하는 프로그램을 작성하시오.
 
 [접근]
 이 문제는 d개의 도토리가 들어있는 상자 중 가장 작은 값을 찾으면 되는 문제
 
 1. 일단 임의의 상자를 둔다 = mid
 2. mid < rules:start 인 경우, continue
 3. 아닌 경우, end 범위 조정해주고
 4. rule에 맞춰서 도토리 개수 구해주기 > res += (e - s) // j + 1
 :: (100,150,10) 
'''

n, k, d = map(int, input().split())
rules = []
for _ in range(k):
    rules.append(list(map(int, input().split())))

def check(m):
    res = 0
    for s, e, j in rules:
        if m < s:
            continue
        e = min(e, m)
        res += (e - s) // j + 1
    
    '''
    if res >= d:
        return True
    else:
        return False
    '''    
    
    return res >= d

def binary_search():
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start
print(binary_search())
            