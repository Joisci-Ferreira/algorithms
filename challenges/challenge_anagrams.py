def merge(string, start, end):
    left = string[end]
    next = start - 1
    for i in range(start, end):
        if string[i] <= left:
            next = next + 1
            string[i], string[next] = string[next], string[i]
    string[next + 1], string[end] = string[end], string[next + 1]
    result = next + 1
    return result


def sort(string, start, end):
    if start < end:
        left = merge(string, start, end)
        sort(string, start, left - 1)
        sort(string, left + 1, end)
    return string


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if not (first_string or second_string):
        return ('', '', False)
    if first_string == '' and second_string == '':
        return ('', '', False)
    merge1 = list(first_string.lower())
    merge2 = list(second_string.lower())
    merge1_sort = sort(merge1, 0, len(merge1) - 1)
    merge2_sort = sort(merge2, 0, len(merge2) - 1)
    result = (
            ''.join(merge1_sort),
            ''.join(merge2_sort),
            merge1_sort == merge2_sort
            )
    return result        