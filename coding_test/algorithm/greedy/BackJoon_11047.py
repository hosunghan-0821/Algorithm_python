def solution():
    n, k = map(int, input().split())
    coin = list()
    count = 0
    for i in range(n):
        coin.append(int(input()))

    coin.sort(reverse=True)
    for data in coin:
        if k == 0:
            break

        if data > k:
            continue
        count += k // data
        k -= ((k // data) * data)

    return count


if __name__ == "__main__":
    print(solution())