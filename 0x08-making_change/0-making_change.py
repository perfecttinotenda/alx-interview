#!/usr/bin/python3
"""
    This is a change making module.
"""


def makeChange(coins, total):
    """
        This will determine the fewest num yema coins needed to meet a given
        num total if wen given a pile of the coins of diff vals.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count