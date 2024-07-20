# Part 1 #
def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp


# basically here we want to sort the hands and bids based on the sort rules the question showed.
hand_strength = {'Five of kind': 7, 'Four of kind': 6, 'Full house': 5,
                      'Three of kind': 4, 'Two pair': 3, 'One pair': 2, 'High card': 1}
card_strength = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7,
                      '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


def card_type(hand):
    chars_dict = {}
    for card in hand:
        if card in chars_dict:
            chars_dict[card] += 1
        else:
            chars_dict[card] = 1

    if len(chars_dict) == 1:
        return 'Five of kind'
    if len(chars_dict) == 2:
        if 4 in chars_dict.values():
            return 'Four of kind'
        else:
            return 'Full house'
    if len(chars_dict) == 3:
        if 3 in chars_dict.values():
            return 'Three of kind'
        else:
            return 'Two pair'
    if len(chars_dict) == 4:
        return 'One pair'
    if len(chars_dict) == 5:
        return 'High card'

def card_type2(hand):
    chars_dict = {}
    for card in hand:
        if card in chars_dict:
            chars_dict[card] += 1
        else:
            chars_dict[card] = 1
    if 'J' in chars_dict:
        # add j count to the highest possible count
        max_val = 0
        max_char = 0
        for k, v in chars_dict.items():
            if k != 'J' and v > max_val:
                max_val = chars_dict[k]
                max_char = k
        if max_char != 0:
            chars_dict[max_char] += chars_dict['J']
            chars_dict.pop('J')

    if len(chars_dict) == 1:
        return 'Five of kind'
    if len(chars_dict) == 2:
        if 4 in chars_dict.values():
            return 'Four of kind'
        else:
            return 'Full house'
    if len(chars_dict) == 3:
        if 3 in chars_dict.values():
            return 'Three of kind'
        else:
            return 'Two pair'
    if len(chars_dict) == 4:
        return 'One pair'
    if len(chars_dict) == 5:
        return 'High card'


def sort_hands_by_rank(hands, bids):
    quicksort_helper(hands, bids, 0, len(hands) - 1)


def quicksort_helper(hands, bids, low, high):
    if low < high:
        pivot = hands[(low + high) // 2]
        index = partition(hands, bids, low, high, pivot)
        quicksort_helper(hands, bids, low, index - 1)
        quicksort_helper(hands, bids, index, high)


def partition(hands, bids, low, high, pivot):
    while low <= high:
        while is_left_greater(pivot, hands[low]):
            low += 1
        while is_left_greater(hands[high], pivot):
            high -= 1
        if low <= high:
            swap(hands, low, high)
            swap(bids, low, high)
            low += 1
            high -= 1
    return low


def is_left_greater(left_hand, right_hand):
    left_strength = hand_strength[card_type2(left_hand)]
    right_strength = hand_strength[card_type2(right_hand)]
    if left_strength > right_strength:
        return True
    elif left_strength == right_strength:
        for i in range(5):
            if card_strength[left_hand[i]] > card_strength[right_hand[i]]:
                return True
            elif card_strength[left_hand[i]] < card_strength[right_hand[i]]:
                return False
    return False


def count_total_winnings():
    with (open("input.txt", "r") as input_file):
        hands_n_bids = [(line.split()[0], line.split()[1]) for line in input_file.readlines()]
        hands = [tup[0] for tup in hands_n_bids]
        bids = [tup[1] for tup in hands_n_bids]
        winnings = 0
        sort_hands_by_rank(hands, bids)
        for i in range(len(hands)):
            winnings += (i+1) * int(bids[i])

    print(winnings)


if __name__ == "__main__":
    count_total_winnings()
