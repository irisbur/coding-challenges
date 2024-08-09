# A solution with RegEx.

import re


def is_valid_ipv6_rg(ip):
    p = r"[0-9A-Fa-f]{1,4}"
    pattern = (r"^(" + p + r")\:(" + p + r")\:(" + p + r")\:(" + p + r")\:(" + p + r")\:(" + p + r")\:(" + p + r")\:(" +
               p + r")$")
    p = re.compile(pattern)
    return bool(p.fullmatch(ip))


def is_valid_ipv4_rg(ip):
    p = r"[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]"
    full_pattern = r"^(" + p + r")\.(" + p + r")\.(" + p + r")\.(" + p + r")$"
    p = re.compile(full_pattern)
    return bool(p.fullmatch(ip))


# A solution without RegEx.
def valid_ip_address(queryIP: str) -> str:
    if is_valid_ipv4(queryIP):
        return "IPv4"
    if is_valid_ipv6(queryIP):
        return "IPv6"
    return "Neither"


def is_valid_ipv6(ip):
    items = ip.split(':')
    if len(items) != 8:
        return False

    for val in items:
        if not is_valid6(val):
            return False
    return True


def is_valid6(val):
    if val == "" or len(val) > 4:
        return False
    for c in val:
        if not (c.isdigit() or ('a' <= c.lower() <= 'f')):
            return False
    return True


def is_valid_ipv4(ip):
    items = ip.split('.')
    if len(items) != 4:
        return False

    for val in items:
        if not is_valid4(val):
            return False
    return True


def is_valid4(val):
    if val == "" or len(val) > 3 or not val.isdigit():
        return False
    if len(val) > 1 and val[0] == '0':
        return False
    return 0 <= int(val) <= 255
