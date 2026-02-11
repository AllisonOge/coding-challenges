# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: determine winner of the prime game over x rounds.


def _prime_counts_up_to(n):
    """Build prefix counts where counts[i] = number of primes <= i."""
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
        p += 1

    counts = [0] * (n + 1)
    running = 0
    for i in range(1, n + 1):
        if sieve[i]:
            running += 1
        counts[i] = running
    return counts


def is_winner(x, nums):
    """Return winner name ('Maria' or 'Ben'), or None for a tie.

    Mental roadmap:
    1. Precompute number of primes up to every n (sieve + prefix count).
    2. In a round with value n, moves available equal prime_count[n].
    3. Odd move count => first player (Maria) wins that round.
    4. Even move count => second player (Ben) wins that round.
    5. Count round wins and return overall winner.

    Toy example:
    n=5 has primes [2,3,5] -> 3 moves (odd) -> Maria wins round.
    n=4 has primes [2,3] -> 2 moves (even) -> Ben wins round.
    Why effective:
    Round outcomes reduce to parity, and precomputation makes many rounds fast.
    """
    if x < 1 or not nums:
        return None

    limit = max(nums)
    prime_counts = _prime_counts_up_to(limit)

    maria_wins = 0
    ben_wins = 0
    for n in nums[:x]:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
