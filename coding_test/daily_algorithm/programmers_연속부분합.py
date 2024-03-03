def solution(sequence, k):
    answer = []

    for i in range(len(sequence)):
        temp = k
        start_index = i
        if temp >= sequence[i]:
            temp -= sequence[i]

        if temp == 0:
            answer.append((start_index, start_index, 0))

        for j in range(i + 1, len(sequence)):

            end_index = j

            if temp >= sequence[j]:
                temp -= sequence[j]
            else:
                break
            if temp == 0:
                answer.append((start_index, end_index, end_index - start_index))
                break

    answer.sort(key=lambda x: (x[2], x[1]))
    return_value = [answer[0][0], answer[0][1]]
    return return_value