import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    data = list()
    n = int(input())
    result = 0

    for j in range(n):
        s1, s2 = map(int, input())
        data.append((s1, s2))

    data.sort(key=lambda x: x[0])
    grade = data[0][1]
    result = 1

    for j in range(1, n):
        if data[j][1] < grade:
            result += 1
            grade = data[j][1]

    print(result)