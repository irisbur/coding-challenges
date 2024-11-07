

def is_valid(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    pairs_ind = []
    count_pairs = 0
    for i in range(1, len(password)):
        if password[i-1] == password[i]:
            count_pairs += 1
            pairs_ind.append(i-1)

    count_pairs = 0
    pairs_ind.sort()
    for j in range(1, len(pairs_ind)):
        if pairs_ind[j] - pairs_ind[j - 1] > 1:
            count_pairs += 1

    for i in range(2, len(password)):
        if (ord(password[i-1]) - ord(password[i-2]) == 1) and (ord(password[i]) - ord(password[i-1]) == 1):
            return count_pairs >= 1
    return False


def increment_password(password):
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        ch = password[i]
        if password[i] != 'z':
            password[i] = chr(ord(ch) + 1)
            break
        else:
            password[i] = 'a'
            i -= 1

    while 'i' in password or 'o' in password or 'l' in password:
        if 'i' in password:
            i_ind = password.index('i')
            password[i_ind] = 'j'
            password[i_ind + 1:] = ['a'] * (len(password) - i_ind - 1)

        if 'o' in password:
            i_ind = password.index('o')
            password[i_ind] = 'p'
            password[i_ind + 1:] = ['a'] * (len(password) - i_ind - 1)

        if 'l' in password:
            i_ind = password.index('l')
            password[i_ind] = 'm'
            password[i_ind + 1:] = ['a'] * (len(password) - i_ind - 1)

    return ''.join(password)


def find_next_password(password):
    cur_pass = password
    while not is_valid(cur_pass):
        cur_pass = increment_password(cur_pass)
    return cur_pass


print(find_next_password(""))
