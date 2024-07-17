import math


# Part 1 #

# The question actually asks how many integers are above
# the given distance (d) in the function t*x - x^2
# where t is the total given time and x is the amount
# of time were holding the button of the boat.
# The number of option is the floor of the difference between
# x_1 and x_2 for the eq x^2 -tx + d > 0
def count_ways_for_race(t, d):
    x1 = math.floor((t + math.sqrt(t ** 2 - 4 * d)) / 2)
    x2 = math.ceil((t - math.sqrt(t ** 2 - 4 * d)) / 2)
    ways = int(math.floor(x1) - math.floor(x2))
    if t*x1 - x1**2 == d:
        ways -= 1
    if t*x2 - x2**2 == d:
        ways -= 1
    return ways + 1


def count_ways_in_races():
    with open("input.txt", "r") as input_file:
        times = input_file.readline().split(':')[1].split()
        distances = input_file.readline().split(':')[1].split()
        total_ways = 1
        for i in range(len(times)):
            total_ways *= count_ways_for_race(int(times[i]), int(distances[i]))

    print(total_ways)


if __name__ == "__main__":
    count_ways_in_races()
