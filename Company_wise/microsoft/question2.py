# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    char_dict = dict()
    for char in S:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char]  = 1

    result = 0
    for key in char_dict:
        total_count_key = char_dict[key]
        value_list = char_dict.values()
        while value_list.count(total_count_key) > 1:
            char_dict[key] -= 1
            total_count_key = char_dict[key]
            result+=1
        char_dict[key] = total_count_key

    return result


test1 = "aaaabbbb"
test2 = "cccaaffddeee"
# test2 = "cddeee"
print solution(test2)
