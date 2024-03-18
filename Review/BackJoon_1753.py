import sys
import heapq

n, m = map(int, input().split())
start_node = int(input())
INF = 10 ** 7
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

q = [] 
distance[start_node] = 0
heapq.heappush(q, (0, start_node))

while q:
    dist, node = heapq.heappop(q)

    if distance[node] < dist:
        continue

    for end, cost in graph[node]:
        new_cost = cost + dist

        if new_cost < distance[end]:
            distance[end] = new_cost
            heapq.heappush(q, (new_cost, end))

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

