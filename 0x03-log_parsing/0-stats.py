#!/usr/bin/python3
"""Log parsing"""

import sys


def print_metrics(status_counts, total_size):
    """Log parsing"""
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def main():
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    count = 0
    total_size = 0

    try:
        for line in sys.stdin:
            if count != 0 and count % 10 == 0:
                print_metrics(status_counts, total_size)

            parts = line.split()
            count += 1

            try:
                total_size += int(parts[-1])
            except (ValueError, IndexError):
                pass

            try:
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

        print_metrics(status_counts, total_size)

    except KeyboardInterrupt:
        print_metrics(status_counts, total_size)
        raise


if __name__ == "__main__":
    main()
