"""
You are building a VOD app which displays videos from two channels(for example, HBO videos and ABC videos).
Specifically, we're building the "recently released videos" page, for which you need to return the list of
recently released videos - newest first, oldest last.
//
// Input: 2 channels, each channel is a list of O(n) videos, already sorted by release date.
// Output: One list, sorted by release date.
"""

def is_date_greater(date1, date2):  # 1, if date 1 is greater, 0 equal, -1 date 2 is gearter
    pass


def merge_sorted_arrays(lst1, lst2):  # each val is (movie_name as string, date as Date )
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if is_date_greater(lst1[i][1], lst2[j][1]) >= 0:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    if i < len(lst1):
        result += lst1[i:]

    if j < len(lst2):
        result += lst2[j:]

    return result


def find_next_item(channels, pointer_in_channel):
    items = []
    for i, channel in enumerate(channels):
        if pointer_in_channel > 0:
            items.append((channel[len(channel) - i], i))

    items.sort(key=lambda x: x[2])  # sort by release date

    return items[0][2], items[0][:2]


def merge_k_sorted_channels(channels):
    result = []
    pointer_in_channel = [len(channel) - 1 for channel in channels]
    while 0 not in pointer_in_channel:
        # find smallest value from k lists
        list_index, smallest = find_next_item(channels, pointer_in_channel)

        result.append(smallest)
        pointer_in_channel[list_index] -= 1
    return result

