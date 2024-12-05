

def parse_input_for_part_1():
    with (open('input.txt') as f):
        lines = f.readlines()
        rules = dict()
        v = set()
        for line in lines[:21]:
            line = line.split('|')
            a, b = int(line[0]), int(line[1])
            v.add(a)
            v.add(b)
            if b in rules:
                rules[b].append(a)
            else:
                rules[b] = [a]

        updates = [line.split(',') for line in lines[22:]]
        new_updates = []
        for update in updates:
            new_updates.append([int(n) for n in update])

    return rules, list(v), new_updates

def is_update_correct(rules, update):
    is_correct = True
    for i, page in enumerate(update):
        if page in rules:
            for constraint in rules[page]:
                if constraint not in update[:i] and constraint in update:
                    is_correct = False
    return is_correct

def count_correct_middle_pages():
    rules, ve, updates = parse_input_for_part_1()
    middles_sum = 0
    for update in updates:
        if is_update_correct(rules, update):
            middles_sum += update[len(update) // 2]
    return middles_sum

def sort_helper(ve, v, visited, stack, rules):
    visited[v] = True

    for i in rules[v]:
        if not visited[i]:
            sort_helper(ve, i, visited, stack)

    stack.insert(0, v)

# sort topological
def fix_update(rules, update):
    visited = [False] * len(update)
    stack = []

    for i in range(len(update)):
        if not visited[i]:
            sort_helper(update, i, visited, stack, rules)

    return stack


def count_wrong_middle_pages():
    rules, ve, updates = parse_input()
    middles_sum = 0
    for update in updates:
        if not is_update_correct(rules, update):
            sorted_update = fix_update(rules, update)
            middles_sum += update[len(sorted_update) // 2]
    return middles_sum


if __name__ == '__main__':
    print(count_wrong_middle_pages())