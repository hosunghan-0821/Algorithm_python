import sys
import heapq

input = sys.stdin.readline

N, M, start = map(int, input().split())

graph = [[] for i in range(N + 1)]
# graph 만들기
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

# distance
distance = [10e7] * (N + 1)

q = []
distance[start] = 0
heapq.heappush(q, (0,start))
# q가 빌 동안
while q:
    dist, end = heapq.heappop(q)

    # distance 값이 작다면 무시 해도 됨
    if distance[end] < dist:
        continue

    # 최소값이 변경되어야 함  // end 까지의 길이가 달라졌기 때문에
    for i in graph[end]:
        new_cost = i[1] + dist
        if new_cost < distance[i[0]]:
            distance[i[0]] = new_cost
            heapq.heappush(q, (new_cost,i[0]))

count = 0
max_value =-1

for i in distance:
    if i != 10e7 and i != 0:
        count += 1
        if i > max_value:
            max_value = i

print(count, max_value)