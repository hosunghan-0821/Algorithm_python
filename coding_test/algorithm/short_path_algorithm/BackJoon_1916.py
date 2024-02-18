import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [1e8] * (N + 1)

for i in range(M):
    # 그래프 초기화
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())
distance[start] = 0
q = []
heapq.heappush(q, (start, 0))
while q:
    start, cost = heapq.heappop(q)
    if distance[start] < cost:
        continue

    for i in graph[start]:
        added_cost = cost + i[1]

        if added_cost < distance[i[0]]:
            distance[i[0]] = added_cost
            heapq.heappush(q, (i[0], added_cost))

print(distance[end])
