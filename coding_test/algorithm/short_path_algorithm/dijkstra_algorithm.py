import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드 입력 받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 것을 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 큐에서 꺼낸 다른 목적지의까지의 거리 와, 저장되어있는 최소 거리를 비교
        if distance[now] < dist:
            continue

        for i in graph[now]:
            # 간선에 연결되어있는 다른 노드로 가기위한 비용 계산
            cost = dist + i[1]

            # 계산된 값이 기존의 코스트 보다 작다면
            # 최소 값 갱신하고, heap에 넣어서 갈 수 있는 곳들에 대한 값 다시 체크해야함.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("no")
    else:
        print(distance[i])