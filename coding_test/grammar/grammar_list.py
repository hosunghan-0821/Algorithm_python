def list_example():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 일정 구간 print 하기
    print(f"일정 구간 print 하기 \n {a[1:4]} \n")

    # 0부터 9까지의 수를 포함하는 리스트 초기화 하기
    array = [i for i in range(1, 10) if i % 2 == 1]

    # array 내림차순 정렬
    array.sort(reverse=True)

    print(f"array 내림차순 정렬 데이터 \n {array} \n")

    # 2차원 배열 List 초기화
    n = 4
    m = 3

    array = [[0] * m for _ in range(n)]
    print(f"2차원 배열 List 초기화 데이터 \n {array} \n")

    # 리스트에서 특정 값을 가지는 원소 모두 제거하기

    a = {1, 2, 3, 4, 5, 5, 5}
    remove_set = {3, 5}
    result = [i for i in a if i not in remove_set]
    print(f"리스트에서 특정 값을 가지는 원소 모두 제거하기 \n {result} \n")


if __name__ == '__main__':
    list_example()
