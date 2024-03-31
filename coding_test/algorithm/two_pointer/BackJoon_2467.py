import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

left = 0
right = n - 1

left_value = data[left]
right_value = data[right]

min_value = abs(data[right] + data[left])

while left != right - 1:

    value1 = abs(data[left + 1] + data[right])
    value2 = abs(data[left] + data[right - 1])

    if value1 < value2:
        if min_value > value1:
            min_value = value1
            left_value = data[left + 1]
            right_value = data[right]
        left += 1
    else:
        if min_value > value2:
            min_value = value2
            left_value = data[left]
            right_value = data[right - 1]
        right -= 1

    if min_value == 0:
        break

print(left_value, right_value)
