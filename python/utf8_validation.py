# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: validate that a list of integers is valid UTF-8.


def valid_utf8(data):
    """Return True if data represents a valid UTF-8 byte stream.

    Mental roadmap:
    1. Read one byte at a time.
    2. If not inside a multi-byte char, detect lead-byte pattern.
    3. Track how many continuation bytes are expected.
    4. Each continuation byte must start with bits ``10``.

    Toy example:
    [197, 130, 1]
    197 starts a 2-byte char -> expect 1 continuation.
    130 matches ``10xxxxxx`` -> continuation satisfied.
    1 is valid single-byte char -> stream valid.
    Why effective:
    UTF-8 validity is defined by these bit-prefix rules.
    """
    remaining = 0

    for value in data:
        byte = value & 0xFF

        if remaining == 0:
            if (byte >> 7) == 0b0:
                continue
            if (byte >> 5) == 0b110:
                remaining = 1
            elif (byte >> 4) == 0b1110:
                remaining = 2
            elif (byte >> 3) == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            remaining -= 1

    return remaining == 0
