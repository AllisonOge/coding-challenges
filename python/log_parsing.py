# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: parse HTTP log lines and aggregate status counts and total size.

import re

_VALID_STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]
_LINE_REGEX = re.compile(r"^\S+ - \[.*?\] \"GET /projects/260 HTTP/1\.1\" (\d{3}) (\d+)$")


def parse_log_lines(lines):
    """Parse iterable of log lines.

    :return: (total_size, {status_code: count})

    Mental roadmap:
    1. Validate each line shape with a regex.
    2. Extract status code and file size only from valid lines.
    3. Add file size to running total.
    4. Count only known HTTP status codes.

    Toy example:
    line -> "... 200 1200" increases total by 1200 and count[200] by 1.
    invalid line -> ignored.
    Why effective:
    Parsing is strict and deterministic, so noisy input cannot corrupt stats.
    """
    total_size = 0
    status_counts = {code: 0 for code in _VALID_STATUS_CODES}

    for line in lines:
        match = _LINE_REGEX.match(line.strip())
        if not match:
            continue

        status_code = int(match.group(1))
        file_size = int(match.group(2))
        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1

    return total_size, status_counts
