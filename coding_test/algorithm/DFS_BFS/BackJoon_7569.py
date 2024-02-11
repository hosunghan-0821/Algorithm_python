import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(100000)


graph = []

total_column = 0
total_row = 0
total_height = 0
depth = 0

# 상하좌우 위(z) 아래(z)
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def BFS(queue):
    global dx, dy, dz
    global graph,depth
    global total_column, total_row, total_height

    next_queue = deque()
    while (queue):
        height, row, column = queue.popleft()
        for i in range(6):
            next_height = height + dz[i]
            next_column = column + dx[i]
            next_row = row + dy[i]
            if next_row < 0 or next_row >= total_row or next_column < 0 or next_column >= total_column or next_height < 0 or next_height >= total_height:
                continue
            if graph[next_height][next_row][next_column] == 0:
                graph[next_height][next_row][next_column] = 1
                next_queue.append((next_height, next_row, next_column))

    if len(next_queue) > 0:
        depth += 1
        BFS(next_queue)


def solution():
    global graph, depth
    global total_column, total_row, total_height
    total_column, total_row, total_height = map(int, input().split())
    is_need_bfs = False
    # graph[height][row][column]
    graph = [[[0] * total_column for _ in range(total_row)] for _ in range(total_height)]
    for i in range(total_height):
        for j in range(total_row):
            data = list(map(int, input().split()))
            for k in range(total_column):
                graph[i][j][k] = data[k]

    queue = deque()
    for i in range(total_height):
        for j in range(total_row):
            for k in range(total_column):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
                elif graph[i][j][k] == 0 and is_need_bfs is False:
                    is_need_bfs = True
    if not is_need_bfs:
        return 0
    depth = 0
    BFS(queue)
    for i in range(total_height):
        for j in range(total_row):
            for k in range(total_column):
                if graph[i][j][k] == 0:
                    return -1

    return depth


if __name__ == "__main__":
    print(solution())
