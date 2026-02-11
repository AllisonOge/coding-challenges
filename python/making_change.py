# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: find the minimum number of coins needed to make a total.


def make_change(coins, total):
    """Return the minimum number of coins needed, or -1 if impossible.

    Mental roadmap:
    1. Let ``dp[a]`` mean minimum coins needed to make amount ``a``.
    2. Initialize ``dp[0] = 0`` and others as unreachable.
    3. For each amount, try each coin and relax from smaller subproblems.
    4. Final answer is ``dp[total]`` if reachable.

    Toy example:
    coins=[1,3,4], total=6
    dp[3]=1 (coin 3), dp[6]=2 via dp[3]+coin 3.
    Why effective:
    Dynamic programming guarantees global optimum from optimal substructure.
    """
    if total <= 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return -1 if dp[total] == float("inf") else dp[total]
