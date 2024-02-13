import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    all_list = list(map(int, input().split()))
    plus_list = list()
    minus_list = list()
    for i in range(n):
        if all_list[i] < 0:
            minus_list.append(all_list[i])
        else:
            plus_list.append(all_list[i])

    plus_list.sort()
    minus_list.sort()

    min_value = sys.maxsize
    plus_list_length = len(plus_list)
    minus_list_length = len(minus_list)
    result1: int
    result2: int

    # 최대 + 최대
    if abs(minus_list[0] + plus_list[plus_list_length - 1]) < min_value:
        min_value = abs(minus_list[0] + plus_list[plus_list_length - 1])
        result1 = minus_list[0]
        result2 = plus_list[plus_list_length - 1]

    # 최소 + 최소
    # 0일 때 예외
    if plus_list[0] == 0:
        if abs(minus_list[minus_list_length - 1] + plus_list[1]) < min_value:
            min_value = abs(minus_list[minus_list_length - 1] + plus_list[1])
            result1 = minus_list[minus_list_length - 1]
            result2 = plus_list[1]


    if abs(minus_list[minus_list_length - 1] + plus_list[0]) < abs(plus_list[1] + plus_list[0]):
        if abs(minus_list[minus_list_length - 1] + plus_list[0]) < min_value:
            min_value = abs(minus_list[minus_list_length - 1] + plus_list[0])
            result1 = minus_list[minus_list_length - 1]
            result2 = plus_list[0]
    else:
        if abs(plus_list[1] + plus_list[0]) < min_value:
            result1 = plus_list[0]
            result2 = plus_list[1]

    print(f"{result1} {result2}")


if __name__ == "__main__":
    solution()