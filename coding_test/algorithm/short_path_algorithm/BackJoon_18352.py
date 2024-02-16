import sys
import heapq
from collections import deque

input = sys.stdin.readline

# 거리가 K인 도시의 번호를 오름차순으로 출력
N, M, K, start = map(int, input().split())

# 초기 그래프 세팅
graph = [[] for _ in range(N + 1)]
distance = [1e9] * (N + 1)
visited = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


#BFS 로 접근
queue = deque()
queue.append((start, 0))
visited[start] = 1
result = []
while queue:
    node, distance = queue.popleft()
    distance += 1
    for i in graph[node]:
        if visited[i[0]] == 1:
            continue
        visited[i[0]] = 1
        queue.append((i[0], distance))
        if distance == K:
            result.append((i[0]))


if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)


# 다익스타라 알고리즘 코드

def dijkstra(start):
    q = []
    distance[start] = 0

    heapq.heappush(q, (start, 0))
    while q:

        now_node, cost = heapq.heappop(q)
        # 거리가 기존것이 더 작다면, 확인할 필요가 없다.
        if distance[now_node] < cost:
            continue

        # 거리가 더 작다면, 연결된 노선들을 heap에 넣어서, 추가로 거리가 작아지는지 확인해야함

        for i in graph[now_node]:
            related_node_cost = i[1] + cost
            if related_node_cost < distance[i[0]]:
                distance[i[0]] = related_node_cost
                heapq.heappush(q, (i[0], related_node_cost))

"""
dijkstra(start)
result = []
for i in range(len(distance)):
    if distance[i] == K:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)
"""