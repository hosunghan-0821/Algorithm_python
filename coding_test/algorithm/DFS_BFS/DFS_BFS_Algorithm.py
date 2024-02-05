from collections import deque
import sys

input = sys.stdin.readline
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0
n: int
m: int
graph = []
queue = deque()


def DFSRecursive(graph, row, column):
    global result
    global dx, dy
    if row < 0 or row > n - 1 or column < 0 or column > m - 1:
        return False

    if graph[row][column] == 1:
        return False
    else:
        graph[row][column] = 1
        for i in range(4):
            DFSRecursive(graph, row + dy[i], column + dx[i])
        return True


def solution():
    global result
    global n, m
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    for i in range(4):
        for j in range(5):
            if DFSRecursive(graph, i, j):
                result += 1

    return result


def BFS(row, column):
    global graph
    global queue
    global n, m
    queue.append((row, column))
    while queue:
        data_row, data_column = queue.popleft()
        if graph[data_row][data_column] == 0:
            continue
        for i in range(4):
            if data_row + dy[i] < 0 or data_row + dy[i] >= n or data_column + dx[i] < 0 or data_column + dx[i] >= m:
                continue
            elif graph[data_row + dy[i]][data_column + dx[i]] == 0:
                continue
            elif graph[data_row + dy[i]][data_column + dx[i]] == 1:
                graph[data_row + dy[i]][data_column + dx[i]] = graph[data_row][data_column] + 1
                queue.append((data_row + dy[i], data_column + dx[i]))
def example2():
    global graph
    global n, m
    n, m = map(int, input().split())
    for i in range(n):
        input_string = input().strip()
        graph.append([int(char) for char in input_string])
    BFS(0, 0)
    print(graph[n-1][m-1])


if __name__ == "__main__":
    print(example2())
