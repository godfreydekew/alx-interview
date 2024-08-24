#!/usr/bin/python3
"""
Main file for testing
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    if total == 0:
        return 0
    track_coins = [total + 1] * (total + 1)
    track_coins[0] = 0
    max_coins_needed = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                value = i - coin
                coins_needed = track_coins[value] + 1
                max_coins_needed = min(coins_needed, track_coins[i])
                track_coins[i] = max_coins_needed
    return track_coins[total] if track_coins[total] <= total else -1
