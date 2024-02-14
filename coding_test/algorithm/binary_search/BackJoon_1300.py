import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

"""
# 메모리 초과 코드
for i in range(1,N + 1):
    for j in range(1, N +1):
        data.append(i * j)

print(data[K])
"""
# 범위가 맞는가?
start = 1
end = (N + 1) * (N + 1)
target = K
ans = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)

    if target <= temp:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)

