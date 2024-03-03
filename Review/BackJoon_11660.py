import sys

input = sys.stdin.readline

n, test_num = map(int, input().split())

data = []
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(n):
    row = list(map(int, input().split()))
    data.append(row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + data[i - 1][j - 1] - dp[i - 1][j - 1]

for i in range(test_num):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)

# 시간초과 코드
"""
for i in range(test_num):
    x1,y1,x2,y2 = map(int, input().split())
    result = 0
    for i in range(x1 - 1 ,x2):
        for j in range(y1 - 1 ,y2):
            result += data[j][i]
    print(result)
"""


