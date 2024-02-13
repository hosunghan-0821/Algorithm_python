import sys

input = sys.stdin.readline


def solution():
    test_case_num = int(input())
    for i in range(test_case_num):
        data_num = int(input())
        score_list = list()
        result = 0

        for j in range(data_num):
            score1, score2 = map(int, input().split())
            score_list.append((score1, score2))

        score_list.sort(key=lambda x: x[0])
        max_standard = score_list[0][1]
        result = 1

        for i in range(1, data_num):
            if score_list[i][1] < max_standard:
                result += 1
                max_standard = score_list[i][1]

        print(result)


if __name__ == "__main__":
    solution()