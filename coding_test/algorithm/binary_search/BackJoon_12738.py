N = int(input())
data = list(map(int, input().split()))
number_list = []

number_list.append(data[0])
number_list_length = 1

for i in range(1, N):

    if number_list[number_list_length - 1] < data[i]:
        number_list.append(data[i])
        number_list_length += 1

    else:
        start = 0
        end = number_list_length - 1
        change_index = 0
        while start <= end:

            mid = (start + end) // 2

            if data[i] <= number_list[mid]:
                change_index = mid
                end = mid - 1
            else:
                start = mid + 1

        number_list[change_index] = data[i]

print(number_list_length)