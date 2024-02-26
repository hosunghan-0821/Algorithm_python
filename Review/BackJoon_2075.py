import sys
import heapq

input = sys.stdin.readline

n = int(input())

data = list()

for i in range(n):
    row_data = list(map(int, input().split()))
    for j in range(n):
        if len(data) < 5:
            heapq.heappush(data, row_data[j])
        else :
            if row_data[j] > data[0]:
                heapq.heappop(data)
                heapq.heappush(data,row_data[j])

print(heapq.heappop(data))