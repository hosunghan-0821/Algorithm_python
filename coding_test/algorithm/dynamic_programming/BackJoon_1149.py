import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]


#RGB 이기 때문에 열을 늘 3개
row = n
column = 3



for i in range(1, n):
    for j in range(column):
        if j == 0:
            data[i][j] = min(data[i][j] + data[i - 1][1], data[i][j] + data[i - 1][2])
        if j == 1:
            data[i][j] = min(data[i][j] + data[i - 1][0], data[i][j] + data[i - 1][2])
        if j == 2:
            data[i][j] = min(data[i][j] + data[i - 1][0], data[i][j] + data[i - 1][1])

min_value = sys.maxsize
for j in range(3):
    if data[row - 1][j] < min_value:
        min_value = data[row - 1][j]

print(min_value)