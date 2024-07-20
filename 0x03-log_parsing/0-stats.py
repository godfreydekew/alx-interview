#!/usr/bin/python3
'''
Reads line by line from the stdin and computes metrics
'''
import sys
import re


def initialize_log():
    '''
    Initializes log dictionary and status code list
    '''

    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {"file_size": 0, "code_list": {str(code): 0 for code in status_code}}
    return log


def parse_line(line, regex, log):
    '''
    Uses regular expression to extract status code and file size
    '''

    match = regex.fullmatch(line)
    if match:
        stat_code, file_size = match.group(1, 2)
        log["file_size"] += int(file_size)

        if stat_code.isdecimal():
            log["code_list"][stat_code] += 1

    return log


def print_codes(log):
    '''
    Prints File size and status code count
    '''

    print("File size: {}".format(log['file_size']))
    sorted_code_list = sorted(log["code_list"])

    for code in sorted_code_list:
        if log["code_list"][code]:
            print(f"{code}: {log['code_list'][code]}")


def main():
    '''Creates the regular expression and reads from the stdin'''

    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET '
                       r'/projects/260 HTTP/1.1" (.{3}) (\d+)')
    log = initialize_log()
    line_count = 0

    for line in sys.stdin:
        line = line.strip()

        line_count = line_count + 1
        parse_log = parse_line(line, regex, log)

        if line_count % 10 == 0:
            print_codes(parse_log)


if __name__ == "__main__":
    '''Calling necessary functions'''

    main()
    initialize_log()
