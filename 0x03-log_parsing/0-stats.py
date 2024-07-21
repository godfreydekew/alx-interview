#!/usr/bin/python3
import sys
import signal

# Dictionary to keep track of the count of each status code
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

total_size = 0
line_count = 0

def print_stats():
    """ Print the current statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def handle_interrupt(signal, frame):
    """ Handle the keyboard interrupt (CTRL + C) """
    print_stats()
    sys.exit(0)

# Register the interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            ip = parts[0]
            # Skipping the part that checks the exact format for date and request path
            # Assuming the log format is correct based on the problem statement
            status_code = parts[-2]
            file_size = parts[-1]

            # Check if status_code is a valid integer and within the expected range
            if status_code in status_counts:
                try:
                    file_size = int(file_size)
                    status_counts[status_code] += 1
                    total_size += file_size
                except ValueError:
                    # If file_size is not an integer, skip this line
                    continue

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    handle_interrupt(None, None)
finally:
    print_stats()
