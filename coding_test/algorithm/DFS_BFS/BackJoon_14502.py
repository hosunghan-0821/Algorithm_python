import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

total_row = 0
total_column = 0
graph = []
result = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def BFS(new_graph, queue):
    global dx, dy
    while queue:
        row, column = queue.popleft()
        for i in range(4):
            new_row = row + dy[i]
            new_column = column + dx[i]
            if new_row < 0 or new_row >= total_row or new_column < 0 or new_column >= total_column:
                continue
            if new_graph[new_row][new_column] == 0:
                new_graph[new_row][new_column] = 2

                queue.append((new_row, new_column))


def solution():
    global graph, result
    global total_row, total_column
    total_row, total_column = map(int, input().split())
    # 그래프 초기화
    graph = [[0] * total_column for _ in range(total_row)]

    wall_candidate = list()

    # 그래프 값 삽입
    for i in range(total_row):
        data = list(map(int, input().split()))
        for j in range(total_column):
            graph[i][j] = data[j]
            if data[j] == 0:
                wall_candidate.append((i, j))
    # 벽 후보
    wall_candidate_result = combinations(wall_candidate, 3)

    for wall_candidates in wall_candidate_result:
        graph_new = copy.deepcopy(graph)
        queue = deque()
        # 벽 세우기
        for i in range(3):
            wall_row = wall_candidates[i][0]
            wall_column = wall_candidates[i][1]
            graph_new[wall_row][wall_column] = 1

        # 바이러스 위치 넣기 queue에 넣고 BFS 로 처리
        for i in range(total_row):
            for j in range(total_column):
                if graph_new[i][j] == 2:
                    queue.append((i, j))

        BFS(graph_new, queue)
        safe_zone = 0
        for i in range(total_row):
            for j in range(total_column):
                if graph_new[i][j] == 0:
                    safe_zone += 1

        if safe_zone > result:
            result = safe_zone


if __name__ == "__main__":
    solution()
    print(result)
