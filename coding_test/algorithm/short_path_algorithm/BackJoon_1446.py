# dp 10001
# x까지 dp[x] = min(x, 도착지점 - 시작지점 + 지름길 길이 )
import sys

input = sys.stdin.readline

N, D = map(int, input().split())

dp = [i for i in range(D + 1)]
data = []
for i in range(N):
    a, b, c = map(int, input().split())
    if c <= D and c < b - a :

        data.append((a, b, c))

for i in range(1, D + 1):

    for j in data:
        if i == j[1]:
            dp[i] = min(dp[i], dp[j[0]] + j[2])
        elif i > j[1]:
            dp[i] = min(dp[i], dp[j[1]] + i - j[1])
        else :
            dp[i] = min(dp[i],i)

print(dp[D])