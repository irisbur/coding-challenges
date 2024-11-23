import numpy as np
def parse_ingredients():
    with (open('input.txt') as f):
        lines = f.readlines()
        ingredients = dict()
        for line in lines:
            ingredient = []
            line = line.split(':')
            properties = line[1].split(',')
            for prop in properties:
                prop = prop.split()
                ingredient.append(int(prop[1]))
            ingredients[line[0]] = ingredient
    return ingredients



def create_all_options(lst, k, c_k, i, options):
    n = len(lst)
    if i == n:
        if sum(lst) == k:
            options.append(lst.copy())
        return

    for v in range(c_k + 1):
        lst[i] = v
        create_all_options(lst, k, c_k - v, i + 1, options)

def inner_prod(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] + b[i]
    return res

def scale(v, a):
    s_v = []
    for i in range(len(v)):
        s_v.append(a * v[i])
    return s_v


def find_best_combination(ingredients, options):
    best = 0
    best_option = []
    for option in options:
        all_scaled = []
        cals = 0
        for i, ingredient in enumerate(ingredients):
            scaled = scale(ingredients[ingredient][:4], option[i])
            cals += (ingredients[ingredient][4] * option[i])
            all_scaled.append(scaled)
        all_scaled = np.array(all_scaled)
        sums = np.sum(all_scaled,axis=0)
        sums[sums < 0] = 0
        score = np.prod(sums)
        if cals == 500:
            best = max(best, score)
            best_option = option
    return best, best_option


if __name__ == '__main__':
    ingredients = parse_ingredients()
    print(ingredients)
    options = []
    create_all_options([0,0,0,0], 100,100, 0, options)
    print(find_best_combination(ingredients, options))


