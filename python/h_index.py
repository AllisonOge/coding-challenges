# -*- coding: utf-8 -*-
# @Time : 2023/05/07 08:11
# @Author : AllisonOge from Google Kickstart competition 2021
# @Descirbe: Jorge is a physicist who has published many research papers
# and wants to know how much impact they have had in the academic community.
# To measure impact, he has developed a metric, H-index, to score
# each of his papers based on the number of times it has been cited by other papers.
# Specifically, the H-index score of a researcher is the largest integer H
# such that the researcher has H papers with at least H
# citations each.

# Jorge has written N papers in his lifetime. The i-th paper has Ci citations.
# Each paper was written sequentially in the order provided, and
# the number of citations that each paper has will never change.
# Please help Jorge determine his H-index score after each paper he wrote.
#
# Limits
# Time limit: 50 secqonds per test set.
# Memory limit: 1GB.
# 1 ≤ T ≤ 100.
# 1 ≤ Ci ≤ 10000, for all i.
#
# Test set 1
# 1 ≤ N ≤ 1000.
#
# Test set 2
# 1 ≤ N ≤ 10000.

def h_index(c):
    """determine the h-index score
    Args:
        c (list): citations for every paper written
    Return:
        h_index (list): h-index score after each paper written
    """
    h_index = []

    return h_index

test_cases = int(input())
for t in range(1, test_cases + 1):
    # read the number of paper Jorge wrote
    _ = int(input())
    # read citations for the given papers
    c = list(map(int, input().split()))
    print(f"Case #{t}: {' '.join(h_index(c))}")