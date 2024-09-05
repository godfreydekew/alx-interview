#!/usr/bin/python3
"""0. Prime Game"""


def sieve_of_eratosthenes(prime_list_size):
    """
    Uses the famous Sieve of Eratosthenes
        to find the prime numbers in the given range
    Then from the list of prime players will start picking
        and determine the winner for that specific round
    """
    prime = [True for i in range(prime_list_size + 1)]
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= prime_list_size):
        if (prime[p] is True):
            # Update all multiples of p
            for i in range(p * p, prime_list_size + 1, p):
                prime[i] = False
        p += 1
    return prime


def count_primes_up_to_n(primes, n):
    """Count the number of primes from 1 to n."""
    count = 0
    for i in range(2, n + 1):
        if primes[i]:
            count += 1
    return count


def isWinner(x, nums):
    """
    Determine who the winner is after x rounds of the prime game.
    Maria always goes first, and both play optimally.
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = count_primes_up_to_n(primes, n)

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
