import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

data = list(int(input()) for _ in range(n))

max_number_of_type = 0
for i in range(n):
    if i+k > n:
        number_of_type = len(set(data[i:n] + data[:(i + k) % n] + [c]))
    else:
        number_of_type = len(set(data[i:i+k]+[c]))

    if max_number_of_type < number_of_type:
        max_number_of_type = number_of_type

print(max_number_of_type)