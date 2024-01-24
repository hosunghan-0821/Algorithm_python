def solution():
    n = int(input())
    string_array = list()
    char_rank = dict()
    # 각 문자의 개별 점수를 구했음.
    for i in range(n):
        string_data = input()
        string_array.append(string_data)
        for j in range(len(string_data)):
            if char_rank.get(string_data[j]) is None:
                char_rank[string_data[j]] = pow(10, len(string_data) - j - 1)
            else:
                char_rank[string_data[j]] = char_rank.get(string_data[j]) + pow(10, len(string_data) - j - 1)
    # 점수를 기반으로 정렬해서 튜플로 변환
    sorted_char_rank = sorted(char_rank.items(), key=lambda x: x[1], reverse=True)
    string_change_dict = dict()
    start_num = 9
    for key, value in sorted_char_rank:
        string_change_dict[key] = start_num
        start_num -= 1
    # 이제 환산해서 값을 더하면 됨
    sum = 0
    print(string_change_dict)
    for i in range(len(string_array)):
        change_string_array = list()
        for j in range(len(string_array[i])):
            change_string_array.append(string_change_dict[string_array[i][j]])

        sum += int(''.join(str(x) for x in change_string_array))

    return sum


if __name__ == "__main__":
    print(solution())
