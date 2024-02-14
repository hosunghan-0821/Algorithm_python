import sys

input = sys.stdin.readline

N, C = map(int, input().split())

data = [int(input()) for i in range(N)]
data.sort()

start = 1
end = data[N - 1] - data[0]

ans = 0
# for문을 활용한 2진 탐색
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    sum = 0
    current = data[0]

    for i in range(N - 1):
        if data[i + 1] >= current + mid:
            cnt += 1
            current = data[i + 1]

    if cnt >= C:
        start = mid + 1
        ans = mid

    else:
        end = mid - 1



print(ans)


