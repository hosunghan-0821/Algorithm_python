def greedy_algorithm():
    print("start greedy")


def greedy_example():
    n = 1260
    count = 0
    array = [500, 100, 50, 10]
    for coin in array:
        count += n // coin
        n %= coin

    print(count)


def greedy_example2():
    n, k = map(int, input().split())
    count = 0
    while (n != 1):
        count += 1
        if n % k == 0:
            n /= k
        else:
            n -= 1
    print(count)


def greedy_example3():
    print("example3")
    data: str = input()
    print(len(data))
    result: int = 1
    is_all_zero = True
    for i, char in enumerate(data, start=1):
        print(f"{int(char)}")
        if int(char) != 0 or int(char) != 1:
            is_all_zero = False
            result *= int(char)
    if not is_all_zero:
        print(result)
    else:
        print(0)


def greedy_example3_best():
    data = input()
    result = int(data[0])
    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)


def greedy_example4():
    N = int(input())
    scary_data = list((map(int, input().split())))
    scary_data.sort()

    group_total_count = 0
    group_each_count = 1
    for i in range(0, N):
        if scary_data[i] <= group_each_count:
            group_total_count += 1
            group_each_count = 1
        else:
            group_each_count += 1

    print(group_total_count)


if __name__ == "__main__":
    print("hi")
    greedy_example4()
