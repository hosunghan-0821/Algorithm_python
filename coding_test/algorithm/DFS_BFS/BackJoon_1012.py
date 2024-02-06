import sys

input = sys.stdin.readline
# 좌우상하
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def DFSRecursive(row, column, graph, total_row, total_column):
    global dx, dy

    if row < 0 or row >= total_row or column < 0 or column >= total_column:
        return False
    if graph[row][column] == 0:
        return False
    graph[row][column] = 0
    for i in range(4):
        next_row = row + dy[i]
        next_column = column + dx[i]
        DFSRecursive(next_row, next_column, graph, total_row, total_column)
    return True


def solution():
    total_row, total_column, num = map(int, input().split())
    graph = [[0] * total_column for _ in range(total_row)]
    result = 0
    for i in range(num):
        mu_row, mu_column = map(int, input().split())
        graph[mu_row][mu_column] = 1

    for i in range(total_row):
        for j in range(total_column):
            if (DFSRecursive(i, j, graph, total_row, total_column)):
                result += 1
    print(result)


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        solution()

