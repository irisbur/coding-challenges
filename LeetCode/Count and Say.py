
def count_and_say(n: int) -> str:
    if n == 1:
        return "1"
    seq = "1"

    for i in range(n - 1):
        print(seq)
        new_seq = ''
        count = 1
        prev_d = seq[0]
        for d in seq[1:]:
            if d == prev_d:
                count += 1
            else:
                new_seq += str(count) + prev_d
                prev_d = d
                count = 1
        new_seq += str(count) + prev_d
        seq = new_seq

    return seq
