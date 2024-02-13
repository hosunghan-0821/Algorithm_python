import sys

input = sys.stdin.readline


def binary_search(data, start, end):

    while start <= end:
        mid = (start + end) // 2
        sum = 0
        cnt = 0
        for i in range(len(data)):
            if sum + data[i] > mid:
                cnt += 1
                sum = 0
            sum += data[i]

        if cnt > M - 1:
            start = mid + 1
        else:
            end = mid - 1
            result = mid

    print(result)


N, M = map(int, input().split())
data = list(map(int, input().split()))

low = max(data)
high = sum(data)

binary_search(data, low, high)