'''
위 그림처럼 start 부터 end까지의 문자열이 팰린드롬인지 확인하려고 할 때, 
문자열 [start+1,end-1]이 팰린드롬이라는 사실을 이미 알고 있다면 문자열 전체를 검사할 필요 없이 앞 뒤 두 글자 start와 end만 비교해보면 된다.

즉, 어떤 문자열이 팰린드롬인지 확인하려면 양 끝의 문자가 같은지를 확인하고 양 끝단을 제외한 문자열이 팰린드롬인지 확인하면 된다.

양 끝의 문자가 다르면 -> 팰린드롬 아님
양 끝의 문자가 같을 때, 가운데 문자열이
- 팰린드롬이라면 -> 팰린드롬
- 팰린드롬이 아니라면 -> 팰린드롬 아님
가운데 문자열이 팰린드롬인지 아닌지 모른다면 알 때까지 문자열의 길이를 앞뒤로 하나씩 줄이면서 위의 과정을 반복한다.
가운데 문자열이 팰린드롬인지 아닌지 아는 문자열이 나올때까지 문자열의 범위를 줄여가면서 같은 과정을 계속 반복한다는 점에서 DP 문제라고 할 수 있다!
'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())

'''

def is_pal(str_):
    if str_[:len(str_)//2:] == str_[:len(str_)//2:-1]:
        print(1)
    else:
        print(0)
    
    
for _ in range(m):
    s, e = map(int, input().split())
    str_ = arr[s-1: e]
    is_pal(str_)
'''


dp = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if a[i] == a[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if a[j] == a[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])

