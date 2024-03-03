import sys

input = sys.stdin.readline

string1 = input()
string2 = input()

last_index = 0
length1 = len(string1)
length2 = len(string2)
dp = [1] * length2
for i in range(1, length1):
    before_char_index = 0
    for j in range(length2):

        if string1[i - 1] == string2[j]:
            before_char_index = j
        if string1[i] == string2[j]:
            if j > before_char_index:
                dp[i] = max(dp[j] + 1, dp[i])


print(max(dp))