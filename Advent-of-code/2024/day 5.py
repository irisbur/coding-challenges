

def parse_input_for_part_1(file_name='input.txt', rule_lines=21, update_start=22):
    with (open(file_name) as f):
        lines = f.readlines()
        rules = {}
        vertices = set()

        for line in lines[:rule_lines]:
            a, b = map(int, line.split('|'))
            vertices.update([a, b])
            rules.setdefault(b, []).append(a)

        updates = [list(map(int, line.split(','))) for line in lines[update_start:]]
        return rules, sorted(vertices), updates

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

def sort_helper(update, v, visited, stack, edges):
    visited[update.index(v)] = True

    if v in edges:
        for u in edges[v]:
            if u in update and not visited[update.index(u)]:
                sort_helper(update, u, visited, stack, edges)

    stack.insert(0, v)

# topological sort
def fix_update(update, edges):
    visited = [False] * len(update)
    stack = []

    for i in range(len(update)):
        if not visited[i]:
            sort_helper(update, update[i], visited, stack, edges)

    return stack


def parse_input_for_part_2(file_name='input.txt', rule_lines=1176, update_start=1177):
    with (open(file_name) as f):
        lines = f.readlines()
        vertices = set()
        rules = {}
        edges = {}

        for line in lines[:rule_lines]:
            a, b = map(int, line.split('|'))
            vertices.update([a, b])
            edges.setdefault(a, []).append(b)
            rules.setdefault(b, []).append(a)

        updates = [list(map(int, line.split(','))) for line in lines[update_start:]]
        return vertices, edges, rules, updates

def count_wrong_middle_pages():
    vertices, edges, rules, updates = parse_input_for_part_2()
    middles_sum = 0
    for update in updates:
        if not is_update_correct(rules, update):
            sorted_update = fix_update(update, edges)
            print(sorted_update)
            middles_sum += sorted_update[len(sorted_update) // 2]
    return middles_sum


if __name__ == '__main__':
    print(count_wrong_middle_pages())