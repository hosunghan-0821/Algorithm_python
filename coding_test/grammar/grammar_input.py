import sys


def input_example():
    # Data 입력
    n = int(input())
    # Data 입력 정수형 ""(공백)을 기준으로 데이터 리스트화하기.
    data = list(map(int, input().split()))

    data.sort(reverse=True)
    print(data)

    data = sys.stdin.readline().rstrip()
    print(data, end=" ")


if __name__ == '__main__':
    input_example()
