INF = int(1e9)

# 노드 개수
n = int(input())
# 간선 개수
m = int(input())

# 2차원 리스트 초기화 하고 dp Table 로 사용될 예정
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신에서부터 자기자신까지의 거리는 0 으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선 들어온 값 수정
for _ in range(m):
    # A -> B 비용 C
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("no")
        else :
            print(graph[a][b], end= " ")