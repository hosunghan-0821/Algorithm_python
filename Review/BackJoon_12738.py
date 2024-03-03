import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
lis = []
lis_length = 0

for i in range(len(data)):

    if lis_length != 0:

        if data[i] > lis[lis_length - 1]:
            lis.append(data[i])
            lis_length += 1

        elif check_value < last_value:
            start_index = 0
            end_index = lis_length - 1
            target = 0
            while start_index <= end_index:

                mid = (start_index + end_index) // 2

                if check_value <= lis[mid]:
                    end_index = mid - 1
                    target = mid
                else:
                    start_index = mid + 1
            lis[target] = data[i]

    else:
        lis.append(data[i])
        lis_length += 1

print(lis_length)