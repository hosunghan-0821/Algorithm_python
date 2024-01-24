import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    #  data <=0
    data_minus_list = list()
    # data >0
    data_plus_list = list()

    for i in range(n):
        data = int(input())
        if data <= 0:
            data_minus_list.append(data)
        else:
            data_plus_list.append(data)

    data_minus_list.sort()
    data_plus_list.sort(reverse=True)

    sum = 0



    run_count = 0
    if len(data_minus_list) % 2 == 0:
        run_count = len(data_minus_list) // 2
    else:
        run_count = len(data_minus_list) // 2 + 1

    for i in range(run_count):
        index = i * 2
        if index == len(data_minus_list) - 1:
            sum += data_minus_list[index]
            break
        if data_minus_list[index + 1] <= 0:
            sum += (data_minus_list[index] * data_minus_list[index + 1])

    if len(data_plus_list) % 2 == 0:
        run_count = len(data_plus_list) // 2
    else:
        run_count = len(data_plus_list) // 2 + 1

    for i in range(run_count):
        index = i * 2
        if index == len(data_plus_list) - 1:
            sum += data_plus_list[index]
            break
        if data_plus_list[index+1] == 1 or data_plus_list[index] == 1:
            sum += (data_plus_list[index] + data_plus_list[index + 1])
        elif data_plus_list[index + 1] != 0:
            sum += (data_plus_list[index] * data_plus_list[index + 1])

        else:
            sum += data_plus_list[index]

    return sum


if __name__ == "__main__":
    print(solution())
