import sys

input = sys.stdin.readline


def binary_search(data, start, end, budget):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        sum = 0

        for each_budget in data:
            if mid < each_budget:
                sum += mid
            else:
                sum += each_budget

        if sum > budget:
            end = mid - 1

        else:
            start = mid + 1
            result = mid

    print(result)


def solution():
    n = int(input())
    data = list(map(int, input().split()))
    budget = int(input())

    data.sort()
    if budget >= sum(data):
        print(max(data))
        return

    start = 0
    end = data[n - 1]

    binary_search(data, start, end, budget)


if __name__ == "__main__":
    solution()