import sys
input = sys.stdin.readline


n = int(input())
data = [input().strip() for _ in range(n)]

result =[]


for i in range(n):

    word = data[i]
    length = len(word)

    left = 0
    right = length - 1

    is_checked = False
    is_not_palidrome = False

    while left < right:
        # print(left,right)
        if word[right] == word[left]:
            left += 1
            right -= 1
            continue

        else :
            if left < right - 1:
                temp = word[:right] + word[right + 1:]
                if temp[:] == temp[::-1]:
                    is_checked = True
                    break
            if left + 1 < right:
                temp = word[:left] + word[left + 1:]
                if temp[:] == temp[::-1]:
                    is_checked = True
                    break

            is_not_palidrome = True
            break


    if is_checked is True:
        result.append(1)
        continue

    if is_not_palidrome is True:
        result.append(2)
        continue

    result.append(0)


for data in result:
    print(data)