import sys

input = sys.stdin.readline

n,m = map(int, input().split())

dp = [[1e9] * (n + 1) for _ in range(n + 1)]

#좌표 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dp[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1

x, k = map(int, input().split())

for c in range(1, 1 + n):
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            dp[a][b] = min(dp[a][b], dp[a][c] + dp[c][b])

result = -1
if dp[1][k] != 1e9 and dp[k][x] != 1e9:
    print(dp[1][k] + dp[k][x])
else :
    print(-1)