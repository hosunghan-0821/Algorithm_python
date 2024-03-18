import sys

input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int,input().split()))
left = 0
right = K - 1
data_sum = sum(data[left:right + 1])
print(data_sum)
