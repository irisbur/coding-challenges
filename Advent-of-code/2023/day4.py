# Part 1 #

def calculate_score_from_card(winning_numbers, elf_numbers):
    score = 0
    for number in elf_numbers:
        if number in winning_numbers:
            score = 1 if score < 1 else score * 2
    return score


def print_cards_score():
    with open("input.txt", "r") as input_file:
        score = 0
        lines = input_file.readlines()
        for line in lines:
            winning_numbers = line.split(":")[1].split("|")[0].split()
            elf_numbers = line.split(":")[1].split("|")[1][:-1].split()
            score += calculate_score_from_card(winning_numbers, elf_numbers)
    print(score)


# Part 2 #


def calculate_card_stats(winning_numbers, elf_numbers):
    matching_cards = 0
    for number in elf_numbers:
        if number in winning_numbers:
            matching_cards += 1
    return matching_cards


def print_cards_score_with_copies():
    with open("input.txt", "r") as input_file:
        matches = []
        copies_count = [1] * 196
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            winning_numbers = line.split(":")[1].split("|")[0].split()
            elf_numbers = line.split(":")[1].split("|")[1][:-1].split()
            matching_cards = calculate_card_stats(winning_numbers, elf_numbers)
            matches.append(matching_cards)
            for j in range(matching_cards):
                if i+j+1 < 196:
                    copies_count[i+j+1] += copies_count[i]
    print(sum(copies_count))


if __name__ == "__main__":
    print_cards_score_with_copies()
