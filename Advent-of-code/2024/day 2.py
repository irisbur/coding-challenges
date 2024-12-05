
def parse_input():
    with (open('input.txt') as f):
        lines = f.readlines()
        reports = [list(map(int, line.split(' '))) for line in lines]
        return reports


def sign(x):
    if x > 0:
        return 1
    return 0 if x  == 0 else -1

def is_report_safe(report, is_pd):
    diff = 0
    is_safe = True
    for i in range(1, len(report)):
        cur_diff = report[i] - report[i - 1]
        if diff != 0 and sign(diff) != sign(cur_diff):
            is_safe = False
        elif not 1 <= abs(cur_diff) <= 3:
            is_safe = False
        diff = cur_diff

    return is_safe


def safe_reports_count(reports):
    count = 0
    for report in reports:
        if is_report_safe(report, False):
            count += 1
    return count

if __name__ == '__main__':
    reports = parse_input()
    print(safe_reports_count(reports))
