import sys
import copy
input = sys.stdin.readline


# 선택정렬 O(n^2)
# [3, 0, 1] -> index 0,1,2 중 최소 값 index 0 / index 1, 2 중 최소 값 index1
def select_sort(array):
    print("select sort start")
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j

        array[min_index], array[i] = array[i], array[min_index]
    print(array)


# 삽입정렬 O(n^2)
# [3, 0, 1] -> index 1, 0 /  index 2, 1 / index 1, 0 비교
def insert_sort(array):
    print("insert sort start")
    length = len(array)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

    print(array)


# 퀵정렬 O(nlogn)
# [2, 3, 2, 2, 1]
# pivot 은 start index를 범위 검색은 start+1 ~ end 까지
# pivot 보다 작은 애들, 왼쪽 큰 애들 오른쪽 배열로 설정 후
# quick_sort 를 재귀적으로 호출
def quick_sort(array, start, end):

    if start >= end:
        return array
    pivot = start
    left = start + 1
    right = end
    while left <= right:

        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right >= start + 1 and array[right] >= array[pivot]:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            array[right], array[pivot] = array[pivot], array[right]

    quick_sort(array, start, right - 1)
    quick_sort(array,right + 1, end)

# 퀵정렬 파이썬으로 쉽게하기
def quick_sort_with_python(array):
    print("qucik_sort with python start")


def example1():
    print("example1 start")

    array1 = list(map(int, input().split()))
    array = copy.deepcopy(array1)
    insert_sort(array)
    array = copy.deepcopy(array1)
    select_sort(array)
    array = copy.deepcopy(array1)
    quick_sort(array, 0, len(array1) - 1)
    print(array)
    array = copy.deepcopy(array1)

    quick_sort_with_python(array)


if __name__ == "__main__":
    example1()
