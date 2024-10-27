from typing import List


def count_complete_day_pairs(hours: List[int]) -> int:
    pairs_count = 0
    equivalence_map = [0] * 24
    for i, n in enumerate(hours):
        equivalence_map[n % 24] += 1

    pairs_count += (equivalence_map[0] * (equivalence_map[0] - 1)) // 2
    pairs_count += (equivalence_map[12] * (equivalence_map[12] - 1)) // 2

    for r in range(1, 12):
        pairs_count += (equivalence_map[r] * equivalence_map[24 - r])

    return pairs_count
