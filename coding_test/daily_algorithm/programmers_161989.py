def solution(n, m, section):
    answer = 0

    while True:
        if len(section) == 0:
            break
        max_cnt = 0
        max_index = 0
        # 범위 1 ~ 5까지 순회
        for i in range(1, (1 + n- m) + 1):
            temp_index = i
            temp_cnt = 0
            # 칠해야할 영역 최대개수 및 index 확인
            for data in section:

                if data > i + m:
                    break

                if i <= data < i + m:
                    temp_cnt += 1

            if max_cnt < temp_cnt:
                max_cnt = temp_cnt
                max_index = temp_index

        # section에서 제거작업

        for i in range(max_index,max_index + m):
            if i in section:
                section.remove(i)

        answer += 1

    return answer

print(solution(4,1,[1,2,3,4]))