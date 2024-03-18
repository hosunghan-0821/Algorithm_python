import sys

input = sys.stdin.readline

N, target = map(int, input().split())
start_p = 0
end_p = 1

data = list(map(int, input().split()))

if N == 1:
    if data[start_p] == target:
        print(1)
    else:
        print(0)
else:
    result = 0
    data_sum = data[0]
    while True:
        if data_sum < target:
            if end_p < N:
                data_sum += data[end_p]
                end_p += 1
            else:
                break
        elif data_sum == target:
            result += 1
            data_sum -= data[start_p]
            start_p -= 1
        else:
            data_sum -= data[start_p]
            start_p -= 1

    print(result)
