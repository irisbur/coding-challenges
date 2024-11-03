

def permutations(places):
    places = list(places)
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


def parse_input(file_path):
    distances = {}
    places = set()

    with open(file_path) as f:
        for line in f:
            parts = line.split()
            place1, place2 = parts[0], parts[2]
            distance = int(parts[4])

            places.update([place1, place2])
            distances[tuple(sorted((place1, place2)))] = distance

    return places, distances


def calculate_longest_route(places, distances):
    longest_distance = 0

    for route in permutations(places):
        route_distance = sum(
            distances[tuple(sorted((route[i], route[i + 1])))]
            for i in range(len(route) - 1)
        )
        longest_distance = max(longest_distance, route_distance)

    return longest_distance


def main():
    places, distances = parse_input('input.txt')
    return calculate_longest_route(places, distances)


print(main())
