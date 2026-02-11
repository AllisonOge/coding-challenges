# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: determine whether all lockboxes can be opened.


def can_unlock_all(boxes):
    """Return True if all boxes are reachable from box 0.

    Mental roadmap:
    1. Convert the problem to graph reachability.
    2. Start from box 0 (the only initially open box).
    3. Use a stack to repeatedly open new boxes from keys found.
    4. Track visited boxes to avoid loops/reprocessing.

    Toy example:
    boxes = [[1], [2], []]
    stack=[0] -> open 0, discover 1 -> open 1, discover 2 -> open 2.
    All boxes visited => True.
    Why effective:
    If a box is not visited by traversal, there is no key path to it.
    """
    if not boxes:
        return False

    opened = {0}
    stack = [0]

    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if 0 <= key < len(boxes) and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)
