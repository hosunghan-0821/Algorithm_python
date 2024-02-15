import heapq
import sys

input = sys.stdin.readline

n, m, start = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n)]
distance = [1e9] * (n + 1)

# 비용 받아서 우선 입력해두자
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    queue = []
    # 초기 세팅
    distance[start] = 0
    heapq.heappush(queue,(start, 0))

    while queue:
        node, cost = heapq.heappop(queue)
        # 이미 저장 되어 있는 값이 더 작다면, 그게 최소길이
        if cost > distance[node]:
            continue

        # 그렇지 않다면 지금의 노드에서 갈 수 있는 거리를 재서 가까우면 다시 큐에 넣어서 재정립해줘야함

        for i in graph[node]:

            if distance[i[0]] > i[1] + cost:
                distance[i[0]] = i[1] + cost
                heapq.heappush(queue, (node, i[1] + cost))

dijkstra(start)
max_value = 0
num = 0
print(distance)
for i in range(1, n + 1):

    if distance[i] != 1e9 and distance[i] != 0:
        num += 1
        max_value = max(max_value, distance[i])

print(num, max_value)