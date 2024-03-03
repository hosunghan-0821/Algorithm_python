import sys

input = sys.stdin.readline

n, length = map(int, input().split())
data = []

for i in range(n):
    start, end, cost = map(int, input().split())
    data.append((start, end, cost))

dp = [i for i in range(10001)]
for i in range(1,length + 1):
    dp[i] = dp[i - 1] + 1

    for j in range(n):
        start,end,cost = data[j]
        if end == i:
            dp[i] = min(dp[start] + cost, dp[i])

print(dp[length])