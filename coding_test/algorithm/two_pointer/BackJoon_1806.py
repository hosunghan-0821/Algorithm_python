import sys

input = sys.stdin.readline

N, S = map(int, input().split())
data = list(map(int, input().split()))

left = 0
right = 0

length = len(data)
sum_data = data[0]
answer = sys.maxsize

while right < length and left <= right:
    if sum_data == S:

        if answer > right - left + 1:
            answer = right - left + 1

        right = right + 1
        if right < length:
            sum_data += data[right]

    elif sum_data < S:
        right = right + 1
        if right < length:
            sum_data += data[right]

    else:
        sum_data -= data[left]
        left = left + 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)
