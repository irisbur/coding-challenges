from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    coins.sort()
    coins_amount = [0]

    for i in range(1, amount + 1):
        i_coins_count = 2 ** 31 - 1
        for coin in coins:
            if i - coin >= 0 and coins_amount[i - coin] != -1:
                i_coins_count = min(i_coins_count, 1 + coins_amount[i - coin])
        if i_coins_count == 2 ** 31 - 1:
            i_coins_count = -1
        coins_amount.append(i_coins_count)

    return coins_amount[amount]
