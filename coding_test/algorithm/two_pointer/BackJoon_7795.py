import sys

input = sys.stdin.readline

n = int(input())

answer_collection =[]
for i in range(n):

    a_num, b_num = map(int, input().split())

    a_data = list(set(map(int, input().split())))
    b_data = list(set(map(int, input().split())))

    a_data.sort()
    b_data.sort()

    b_p = 0
    a_p = 0

    b_len = len(b_data)
    a_len = len(a_data)
    answer = 0

    while True:
        if b_p == b_len:
            break

        if b_data[b_p] >= a_data[a_p]:
            if a_p + 1 != a_len:
                a_p += 1
            else:
                break
        else:
            answer += a_len - a_p
            b_p += 1

    answer_collection.append(answer)

for answer in answer_collection:
    print(answer)

