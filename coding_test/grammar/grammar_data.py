string = "abcd"
length = len(string)
string_list = list(string)
for i in range(length // 2):
    temp = string_list[i]
    string_list[i] = string_list[length - 1 - i]
    string_list[length - 1 - i] = temp

print(''.join(string_list))
