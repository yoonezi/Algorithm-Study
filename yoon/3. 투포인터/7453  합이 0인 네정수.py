'''
[문제]
정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.

A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

[입력]
n (1 ≤ n ≤ 4000)

브루트포스로 풀면?
O(N^4)? 그러면.. 4000^4 
print(4000**4 > 10**8 * 12) = True : 시간초과

일단 배열이 네개면 투 포인터를 못쓰니 배열을 두개로 만들어서 풀어보자

✨[Review]
중복체크 생각하는 거에서 진짜 한~참 걸렸네..

[시간복잡도]
처음에 ab, cd을 만드는 데 O(n^2),
정렬하는데 O(n^2 log n),
포인터를 돌리는데 O(n^2)이 걸리므로

총 시간복잡도는 O(n^2 log n)
'''

n = int(input())
arr, brr, crr, drr = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split()) 
    arr.append(a)
    brr.append(b)
    crr.append(c)
    drr.append(d)

ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(arr[i]+brr[j])
        cd.append(crr[i]+drr[j])
ab.sort()
cd.sort()

start = 0
leng = (n*n)-1
end = leng
ans = []
cnt = 0

while 0 <= end and start <= (n*n)-1:
    s = ab[start] + cd[end]
    if s == 0:
        x, y = 1, 1

        while start + x < len(ab) and ab[start] == ab[start + x]:
            x += 1
        
        while end - y >= 0 and cd[end] == cd[end - y]:
            y += 1
        
        cnt += x*y
        start += x
        end -= y
        
        
    elif s < 0:
        start += 1
    else:
        end -= 1
print(cnt)