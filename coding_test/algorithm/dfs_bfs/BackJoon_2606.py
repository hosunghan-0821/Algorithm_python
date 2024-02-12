import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
result = 0
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)


# print(visited)


def BFS(num):
    global result, visited
    queue = deque()

    queue.append(num)
    visited[1] = 1
    while queue:
        data = queue.popleft()
        graph_list = graph[data]
        for i in range(len(graph_list)):
            print(
                f"up result start node = {data}, linked node = {graph_list[i]}, isVisited = {visited[graph_list[i]]} ")
            if visited[graph_list[i]] == 0:
                result += 1
                visited[graph_list[i]] = 1
                queue.append(graph_list[i])


for i in range(m):
    index, node_num = map(int, input().split())
    graph[index].append(node_num)
    graph[node_num].append(index)
# print(graph)

BFS(1)
print(result)
