import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def BFS():
    queue = deque()
    queue.append((0, 0))
    while queue:
        data_row, data_column = queue.popleft()
        for i in range(4):
            next_row = data_row + dy[i]
            next_column = data_column + dx[i]
            if next_row < 0 or next_row >= n or next_column < 0 or next_column >= m:
                continue
            if graph[next_row][next_column] == 0:
                continue
            if graph[next_row][next_column] == 1:
                graph[next_row][next_column] = graph[data_row][data_column] + 1
                queue.append(next_row, next_column)


for i in range(n):
    input_string = input().strip()
    graph.append([int(char) for char in input_string])

BFS()
print(graph[n - 1][m - 1])
