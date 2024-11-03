import math

def all_paths_perms(places):
    perms = [[places[0]]]
    for place in places[1:]:
        new_perms = []
        for p in perms:
            for i in range(len(p)+1):
                cur = p.copy()
                cur.insert(i, place)
                new_perms.append(cur)
        perms = new_perms
    return perms


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        adjacency_list = dict()
        places = []
        for line in lines:
            line = line.split()
            if line[0] not in places:
                places.append(line[0])
            if line[2] not in places:
                places.append(line[2])
            adjacency_list[tuple(sorted((line[0], line[2])))] = int(line[4])
        all_perms = all_paths_perms(places)
        longest_cost = 0
        for path in all_perms:
            cur_cost = 0
            for i in range(len(places) - 1):
                cur_cost += adjacency_list[tuple(sorted((path[i], path[i+1])))]
            longest_cost = max(longest_cost, cur_cost)
        return longest_cost


print(main())
