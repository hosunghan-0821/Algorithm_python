import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 7
N, M = map(int, input().split())
K = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    # 그래프 초기화
    first, end, cost = map(int, input().split())
    graph[first].append((end, cost))

distance = [INF for _ in range(N + 1)]

distance[K] = 0

q = []
heapq.heappush(q, (0, K))

while q:
    cost, di_start = heapq.heappop(q)
    if distance[di_start] < cost :
        continue
    for related_node, related_node_value in graph[di_start]:
        added_cost = cost + related_node_value

        if added_cost < distance[related_node]:
            heapq.heappush(q, (added_cost, related_node))
            distance[related_node] = added_cost

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
