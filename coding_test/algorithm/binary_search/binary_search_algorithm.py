import sys
import bisect
input = sys.stdin.readline


#
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


def binary_search_advanced(array, target, start, end, max_height):
    if start > end:
        return max_height
    mid = (start + end) // 2
    sum = 0
    for i in range(len(array)):
        length = array[i] - mid
        if length > 0:
            sum += length

    if sum >= target:
        if mid > max_height:
            max_height = mid
        return binary_search_advanced(array, target, mid + 1, end, max_height)
    elif sum < target:
        return binary_search_advanced(array, target, start, mid - 1, max_height)


def example1():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    result = binary_search_advanced(data, M, 0, data[N - 1], 0)
    print(result)

def example2():
    N, M = map(int ,input().split())
    data = list(map(int, input().split()))

    left_index=bisect.bisect_left(data,M)
    right_index = bisect.bisect_right(data, M)

    print(f"left_index = {left_index}")
    print(f"right_index = {right_index}")
    if (left_index - right_index == 0):
        print(-1)
    print(right_index-left_index)


if __name__ == "__main__":
    example2()
