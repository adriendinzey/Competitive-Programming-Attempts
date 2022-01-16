
longest_substring = ""
longest_length = 0

def main():

    in_str = sys.stdin.readlines()
    string_arr = []

    for sub in in_str:
        string_arr.append(re.sub('\n', '', sub))

    string_arr.pop(0)

    print(len(find_smallest_string(string_arr)))


def find_smallest_string(arr):
    global longest_substring, longest_length
    longest = 0
    l_index = 0

    for s in arr:
        if len(s) > longest:
            l_index = arr.index(s)
            longest = len(s)

    longest_word = arr[l_index]

    start_pos = 0
    sub_length = 1

    while sub_length < longest:
        test_str = longest_word[start_pos:sub_length]

        if all_has_substring(arr, test_str):
            sub_length += 1
        else:
            if len(test_str) > longest_length:
                longest_substring = test_str[0:len(test_str) - 1]
                longest_length = len(test_str)

            start_pos += 1
            sub_length = start_pos + 1

    return longest_substring

def all_has_substring(arr, s):
    has_substring = True
    for full_str in arr:
        has_substring = s in full_str
        if not has_substring:
            has_substring = False
            break

    return has_substring

if __name__ == "__main__":
    main()