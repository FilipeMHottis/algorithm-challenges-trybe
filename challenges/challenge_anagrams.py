def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def is_anagram(first_string, second_string):
    sorted_first_string = "".join(merge_sort(list(first_string.lower())))
    sorted_second_string = "".join(merge_sort(list(second_string.lower())))
    is_anagram = sorted_first_string == sorted_second_string

    if (
        first_string == ""
        or second_string == ""
    ):
        is_anagram = False

    return (sorted_first_string, sorted_second_string, is_anagram)
