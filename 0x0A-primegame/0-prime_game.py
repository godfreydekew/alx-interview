#!/usr/bin/python3
"""0. Prime Game"""


def sieve_of_eratosthenes(prime_list_size: int) -> str | None:
    """
    Uses the famous Sieve of Eratosthenes
        to find the prime numbers in the given range
    Then from the list of prime players will start picking
        and determine the winner for that specific round
    """
    if prime_list_size == 1:
        return "ben"
    ben, maria = 0, 0
    prime = [True for i in range(prime_list_size + 1)]
    p = 2
    while (p * p <= prime_list_size):
        if (prime[p] is True):
            # Update all multiples of p
            for i in range(p * p, prime_list_size + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, prime_list_size + 1):
        if prime[p]:
            if p == 2:
                maria = 1
            elif maria and not ben:
                ben = 1
                maria = 0
            else:
                maria, ben = 1, 0
            # print(winner)
            # print(f"ben : {ben} maria: {maria}")
    if maria:
        return "maria"
    elif ben:
        return "ben"
    else:
        return None


def isWinner(x, nums):
    """
    Using the Sieve of Eratosthenes to determine the winner
    Calculates the overall winner for all the rounds palyed
    """
    if x > len(nums):
        return None
    maria, ben = 0, 0
    for i in range(x):
        winner = sieve_of_eratosthenes(nums[i])
        # print(winner)
        if winner == "maria":
            maria += 1
        if winner == "ben":
            ben += 1
    # print(f"Maria: {maria} ben:{ben}")
    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"
