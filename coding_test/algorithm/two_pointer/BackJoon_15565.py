import sys

input = sys.stdin.readline

N, K = map(int, input().split())

data = list(map(int, input().split()))

left = 0
right = 0
cnt = 0
min_value = sys.maxsize

if data[0] == 1:
    cnt += 1


while right < N:
    if cnt >= K:
        if right - left + 1 < min_value:
            min_value = right - left + 1
        if data[left] == 1:
            cnt -= 1
        left += 1

    else:
        right += 1
        if right < N and data[right] == 1:
            cnt += 1


if min_value == sys.maxsize:
    print(-1)
else :
    print(min_value)