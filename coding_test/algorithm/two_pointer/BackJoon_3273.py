import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
target = int(input())

data.sort()
left = 0
right = 1
result = 0

while data[right] < target:
    if data[right] + data[left] < target:
        right += 1
    elif data[right] + data[left] > target:
        break
    if data[right] + data[left] == target:
        result += 1
        left += 1
        

print(result)