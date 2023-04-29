def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    :param str1: represented as columns in opt
    :param str2: represented as rows in opt
    :return: the longest common subsequence
    """
    if '' in [str1, str2]:
        return ''

    # create opt table
    opt = [[0] * len(str1) for _i in range(len(str2))]
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                opt[i][j] = 1 if 0 in [i, j] else opt[i - 1][j-1] + 1
            else:
                opt[i][j] = 0 if 0 in [i, j] else max(opt[i-1][j], opt[i][j-1])

    # find path from opt table
    sequence = ''
    offset = 0
    for i in range(len(str2)-1, -1, -1):
        for j in range(len(str1)-1-offset, -1, -1):
            offset += 1
            if 0 in [i, j] or opt[i][j] != opt[i][j-1]:
                sequence = str2[i] + sequence
                break
    return sequence


print(longest_common_subsequence('ABCD', 'A'))
