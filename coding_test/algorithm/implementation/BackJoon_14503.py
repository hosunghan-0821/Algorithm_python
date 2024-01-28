import sys

input = sys.stdin.readline


def solution():
    # 0 북 , 1 동, 2 남, 3 서
    total_row, total_column = map(int, input().split())
    row, column, direction = map(int, input().split())
    array = [[0 for _ in range(total_column)] for _ in range(total_row)]
    for i in range(total_row):
        row_data = list(map(int, input().split()))
        for j in range(total_column):
            array[i][j] = row_data[j]

    # column
    dx = [0, 1, 0, -1]
    # row
    dy = [-1, 0, 1, 0]

    count = 0

    while True:
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
        if array[row][column] == 0:
            array[row][column] = 2
            count += 1
        check_another_room = False

        for _ in range(len(dx)):
            # 범위 체크
            if direction == 0:
                direction = 3
            else:
                direction -= 1
            if 0 <= row + dy[direction] < total_row and 0 <= column + dx[direction] < total_column:
                if array[row + dy[direction]][column + dx[direction]] == 0:
                    check_another_room = True
                    row = row + dy[direction]
                    column = column + dx[direction]
                    break
                    # direction 에 따라 쳐다봐야할 방향이 다름
            else:
                continue

        # 4방향 모두 청소될 경우
        if check_another_room is False:

            if direction == 0:
                i = 2
            elif direction == 1:
                i = 3
            elif direction == 2:
                i = 0
            else:
                i = 1
            if 0 <= row + dy[i] < total_row and 0 <= column + dx[i] < total_column:
                if array[row + dy[i]][column + dx[i]] != 1:
                    row = row + dy[i]
                    column = column + dx[i]
                    continue
                elif array[row + dy[i]][column + dx[i]] == 1:
                    break
            else:
                break

    return count


if __name__ == "__main__":
    print(solution())
