import sys
import bisect

input = sys.stdin.readline


#
def binary_search_recursive(array, target, start, end):
    # 종료조건
    if start > end:
        return None

    # 중간값 설정
    mid = (start + end) // 2

    # target 과 비교하면서 다음에 어떻게 할지 정리

    # target 을 찾았으면 mid 값 return
    if target == array[mid]:
        return mid

    # target 이 mid 값 보다 크다면 mid 보다 오른쪽을 검사 해야함
    if target > array[mid]:
        return binary_search_recursive(array, target, mid + 1, end)
    # target 이 mid 값 보다 작다면, mid 보다 왼쪽을 검사 해야함
    if target < array[mid]:
        return binary_search_recursive(array, target, start, mid - 1)


def binary_search_loop(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        if target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1

    return None


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    result = binary_search_recursive(array, 2, 0, (len(array) - 1))
    assert result == 1

    result = binary_search_recursive(array, 0, 0, (len(array) - 1))
    assert result == None

    result = binary_search_loop(array, 0, 0, (len(array) - 1))
    assert result == None

    result = binary_search_loop(array, 8, 0, (len(array) - 1))
    assert result == 7
