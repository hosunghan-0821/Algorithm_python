import sys

input = sys.stdin.readline


def insert_sort(array, length):
    for i in range(1, length):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


def select_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[j] <= array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    print(array)


def quick_sort(array, start, end):
    if start >= end:
        return array

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort_with_python(array, start, end):
    if len(array) <= 1:
        return array

    pivot = array[0]
    divide_array = array[1:]

    left_array = [x for x in divide_array if x <= pivot]
    right_array = [x for x in divide_array if x > pivot]

    return quick_sort_with_python(left_array, 0, 0) + [pivot] + quick_sort_with_python(right_array, 0, 0)


def example1():
    print("example1 start")
    length, change_cnt = map(int, input().split())
    print(length, change_cnt)
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))

    quick_sort(array1, 0, len(array1) - 1)
    print(array1)


if __name__ == "__main__":
    example1()
