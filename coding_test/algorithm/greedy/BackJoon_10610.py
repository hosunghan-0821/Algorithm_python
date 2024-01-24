def solution():
    n = input()
    num = int(n)
    array = [int(digit) for digit in n]

    # 전체의 합이 3으로 나누어 떨어져야 하며, 30 이하의 숫자는 -1
    if len(array) >= 2 and num >= 30:
        # 각 자리수의 합이 3의 배수여야 하고, 0이 포함되어 있어야함
        if sum(array) % 3 == 0 and 0 in array:
            # greedy 로직 수행
            array.sort(reverse=True)
            return ''.join([str(x) for x in array])
        else:
            return -1
    else:
        return -1


if __name__ == "__main__":
    print(solution())
