import sys

input = sys.stdin.readline


def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return fibonacci(n - 1) + fibonacci(n - 2)


def solution():
    print(fibonacci(4))


def example1():
    N = int(input())
    data = list(map(int, input().split(" ")))
    dp = [0] * 100
    dp[0] = data[0]
    dp[1] = data[1] if data[1] > data[0] else data[0]

    for i in range(2, N):
        dp[i] = dp[i - 2] + data[i] if dp[i - 2] + data[i] > dp[i - 1] else dp[i - 1]

    print(dp[N - 1])


def example2():
    n = int(input())
    cnt = 0
    d = [0] * 30001
    for i in range(2, n + 1):
        # 1을 빼는 경우
        d[i] = d[i - 1] + 1

        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    print(d[n])


def example3():
    N, value = map(int, input().split())
    coin_list = [int(input()) for _ in range(N)]
    dp = [10001] * (value + 1)
    dp[0] = 0

    for i in range(N):
        for j in range(coin_list[i], value + 1):
            if dp[j - coin_list[i]] != 10001:
                dp[j] = min(dp[j], dp[j - coin_list[i]] + 1)

    print(dp)
    if dp[value] == 10001:
        print(-1)
    else:
        print(dp[value])


def example4():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    two_dimension_array = []
    index = 0
    for i in range(n):
        array = data[index:index + m]
        index += m
        two_dimension_array.append(array)

    dx = [-1, -1, -1]
    dy = [0, 1, -1]
    print(two_dimension_array)

    # i 열
    # j 행
    for i in range(1, m):
        max_value = 0
        for j in range(n):

            for k in range(3):
                new_column = i + dx[k]
                new_row = j + dy[k]

                if new_row < 0 or new_row >= n or new_column < 0 or new_column >= m:
                    continue

                max_value = max(max_value, two_dimension_array[j][i] + two_dimension_array[new_row][new_column])

            two_dimension_array[j][i] = max_value

    print(two_dimension_array)


def example5():
    N = int(input())
    data = list(map(int, input().split()))
    data.reverse()
    dp= [1] * N

    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)
if __name__ == "__main__":
    example5()
