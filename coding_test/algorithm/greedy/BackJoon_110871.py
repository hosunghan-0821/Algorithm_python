import sys

input = sys.stdin.readline

n = int(input())
time_data = list()

for _ in range(n):
    start_time, end_time = map(int, input().split())
    time_data.append((start_time, 1))
    time_data.append((end_time, -1))

time_data.sort(key=lambda x: (x[0], x[1]))
max_count = 0
room = 0


