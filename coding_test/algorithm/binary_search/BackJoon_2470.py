import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    all_list = list(map(int, input().split()))

    all_list.sort()
    hi_index = len(all_list) - 1
    lo_index = 0
    final_result = [all_list[0], all_list[hi_index]]
    min_value = abs(all_list[0] + all_list[hi_index])
    while lo_index < hi_index:

        left_val = all_list[lo_index]
        right_val = all_list[hi_index]
        sum = left_val + right_val
        if abs(sum) < min_value:
            min_value = abs(sum)
            final_result = [left_val, right_val]

        if sum < 0:
            lo_index += 1
        else :
            hi_index -= 1

    print(f"{final_result[0]} {final_result[1]}")


if __name__ == "__main__":
    solution()