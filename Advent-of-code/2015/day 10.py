
def look_and_say(s, n):
    if not s:
        return ''
    new_s = ''
    for _ in range(n):
        cur_l = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] != cur_l:
                new_s += str(count)
                new_s += str(cur_l)
                cur_l = s[i]
                count = 1
            else:
                count += 1
        new_s += str(count)
        new_s += str(cur_l)
        s = new_s
        new_s = ''
    return s


if __name__ == "__main__":
    print(len(look_and_say("1", 50)))
