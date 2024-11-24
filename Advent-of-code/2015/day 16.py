

def parse_sues():
    with (open('input.txt') as f):
        lines = f.readlines()
        sues = []
        for line in lines:
            properties_map = dict()
            line = line.split()
            for i in range(2, len(line), 2):
                prop = line[i][:-1]
                if (i+1) < (len(line) - 1):
                    line[i+1] = line[i+1][:-1]
                count = int(line[i+1])
                properties_map[prop] = count
            sues.append(properties_map)
    return sues


def find_best_fit_sue(sues, sue_props):
    options = []
    for i, sue in enumerate(sues):
        is_fit = True
        for k, v in sue.items():
            special = ["cats", "trees", "pomeranians", "goldfish"]
            if (k == "cats" or k == "trees") and (sue_props[k] >= sue[k]):
                is_fit = False
            elif (k == "pomeranians" or k == "goldfish") and (sue_props[k] <= sue[k]):
                is_fit = False
            elif k not in special and sue_props[k] != sue[k]:
                is_fit = False
        if is_fit:
            options.append(i+1)
    return options


if __name__ == '__main__':
    sues = parse_sues()

    sues_props = {
        'children': 3, 'cats': 7, 'samoyeds': 2,
        'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
        'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1
    }

    print(find_best_fit_sue(sues, sues_props))
