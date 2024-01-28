import sys

input = sys.stdin.readline


def example_1():
    n = int(input())
    array = [[0 for j in range(n)] for i in range(n)]
    # 0, 1, 2, 3
    # R, L, D, U
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    start_x = 0
    start_y = 0
    direction_list = list(map(str, input().split()))

    for direction in direction_list:
        if direction == 'R' and start_x < n - 1:
            start_x += dx[0]
        elif direction == 'L' and start_x > 0:
            start_x += dx[1]
        elif direction == 'D' and start_y < n - 1:
            start_y += dy[2]
        elif direction == 'U' and start_y > 0:
            start_y += dy[3]

    return start_y + 1, start_x + 1


def example_2():
    n = int(input())
    # n 시 59분 59초
    # hour * 3600 + minute * 60 + sec
    total_sec_count = (n + 1) * 3600
    result = 0
    for i in range(total_sec_count):

        total_sec = i
        hour = i // 3600
        if hour != 0:
            total_sec -= hour * 3600
            if '3' in str(hour):
                result += 1
                continue

        minute = total_sec // 60
        if minute != 0:
            total_sec -= minute * 60
            if '3' in str(minute):
                result += 1
                continue

        sec = total_sec
        if '3' in str(sec):
            result += 1
            continue

    return result


def example_3():
    column_parser = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    input_data = input()
    row = int(input_data[1])
    column = column_parser[input_data[0]]
    print(f"{row} , {column}")

    dx = [2, 1, -2, -1, 2, 1, -2, -1]
    dy = [1, 2, 1, 2, -1, -2, -1, -2]
    count = 0
    for i in range(len(dx)):
        if 0 < row + dy[i] <= 8 and 0 < column + dx[i] <= 8:
            print(f"{dy[i]} {dx[i]} ")
            count += 1

    print(count)
    # 체스 판 8 x 8 이기 떄문에
    # 움직일 수 있는 좌표


def example_4():
    data = input()
    data = data.strip()
    str_data_list = list()

    sum = 0

    for i in range(len(data)):
        data[i].isaplha()
        print(data[i])
        if ord('A') <= ord(data[i]) <= ord('Z'):
            str_data_list.append(data[i])
        else:
            sum += int(data[i])

    str_data_list.sort()
    result = "".join(str_data_list)
    print(f"{result}{sum}")

    


if __name__ == "__main__":
    example_4()
    # print(example_2())
