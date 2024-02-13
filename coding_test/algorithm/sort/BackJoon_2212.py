import sys

input = sys.stdin.readline


# 문제 이해가 제일 어려웠던 문제..
n = int(input())
k = int(input())

data_list = list(map(int, input().split()))
data_list.sort()
distance = []

for i in range(n - 1):
    distance.append(data_list[i + 1] - data_list[i])

distance.sort()

print(sum(distance[:n-k]))