import sys
import heapq

input = sys.stdin.readline


# 메모리 초과로 다른 걸 알아봐야 했음...
def solution():
    data = []
    max_list = []
    dx = [0, 1]
    dy = [1, 0]

    n = int(input())
    for i in range(n):
        data_row = list(map(int, input().split()))
        data_row.sort(reverse=True)
        data.insert(0, data_row)

    result = 0
    result_value = data[0][0]

    max_list.append((0, 0, data[0][0]))
    while result != n:
        # 평가해서 제일 큰 값의 index를 팝해야함
        result += 1
        max_list_index, next_max_value = max(enumerate(max_list), key=lambda x: x[1][2])
        result_value = next_max_value[2]
        row, column, value = max_list.pop(max_list_index)
        for i in range(2):
            new_row = row + dy[i]
            new_column = column + dx[i]
            if new_row >= n or new_column >= n:
                continue
            max_list.append((new_row, new_column, data[new_row][new_column]))

    print(result_value)


def best_practice():
    heap = []
    n = int(input())

    for _ in range(n):
        numbers = map(int, input().split())
        for number in numbers :
            if len(heap) < n:
                heapq.heappush(heap, number)
            else :
                if heap[0] < number:
                    heapq.heappop(heap)
                    heapq.heappush(heap, number)

if __name__ == "__main__":
    best_practice()