import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 8
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end_node = map(int, input().split())

q = []
distance[start] = 0

heapq.heappush(q, (0, start))

while q:

    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue

    for end, cost in graph[node]:
        new_cost = dist + cost
        heapq.heappush(q, (new_cost, end))

print(graph)
print(distance)
print(distance[end_node])





