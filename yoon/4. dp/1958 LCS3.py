'''
[문제]
문자열 3개의 LCS를 구하는 프로그램을 작성하라.

[시간 복잡도]
..?

'''
str1 = input()
str2 = input()
str3 = input()

f = len(str1)
s = len(str2)
t = len(str3)

arr = [[[0] * (t+1) for _ in range(s+1)] for _ in range(f+1)]

for i in range(1, f+1):
    for j in range(1, s+1):
        for k in range(1, t+1):
            if str1[i-1] == str2[j-1] and str2[j-1] == str3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])
                

ans = -1                
for i in range(f+1):
    for j in range(s+1):
        ans = max(max(arr[i][j]), ans)
print(ans)
