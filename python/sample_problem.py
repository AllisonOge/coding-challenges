# -*- coding: utf-8 -*-
# @Time : 2023/05/10 10:53
# @Author : AllisonOge from Google Kickstart competition 2021
# @Descirbe: You have N bags of candy and you want to distribute the candy amongst M kids. The i-th bag contains Ci pieces of candy, and you want to ensure that every child receives the same quantity of candy and that the number of pieces of candy received is the greatest posible. How many pieces of candy will remain after you share?
#
# Limits
# Time limit: 40 seconds per test set.
# Memory limit: 1GB.
#
# Test set 1 (Visible Verdict)
# 1 ≤ T ≤ 100.
# 1 ≤ N ≤ 100000.
# 1 ≤ M ≤ 10000.
# 1 ≤ Ci ≤ 1000, for all i.

test_cases = int(input())
for t in range(1, test_cases+1):
    # read number of candy bags and number of kids
    n, m = list(map(int, input().split()))
    # get the candy amount in N candy bags
    total = sum([ci for ci in list(map(int, input().split()))])
    remainder = total % m
    print(f"Case #{t}: {remainder}")