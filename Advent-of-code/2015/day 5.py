
def is_string_nice(s):
    flag1 = False

    for i in range(1, len(s)):
        if i < (len(s) - 1) and s[i-1] == s[i+1]:
            flag1 = True
            break
        elif i == len(s) - 1:
            return False

    pairs = {}
    for i in range(len(s)):
        if s[i:i+2] in pairs:
            pairs[s[i:i+2]].append(i)
        else:
            pairs[s[i:i+2]] = [i]

    for pair, indices in pairs.items():
        if len(indices) > 1:
            for i in indices:
                for j in indices[1:]:
                    if abs(i-j) > 1:
                        return flag1

    return False


def count_nice_strings():
    with open('input.txt') as f:
        lines = f.readlines()
        nice_strings = 0
        for line in lines:
            if is_string_nice(line[:-1]):
                nice_strings += 1
        return nice_strings


print(count_nice_strings())
