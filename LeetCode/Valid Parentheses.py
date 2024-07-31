
# This solution iterates through the string so the time complexity is O(n) where n is
# the length of the string. The brackets stack might be in a similar length to s so we use
# O(n) space.

def is_valid(s: str) -> bool:
    if s == "":
        return True
    brackets_match = {')': '(', '}': '{', ']': '['}
    brackets_stack = []
    for c in s:
        if c in brackets_match:
            if brackets_stack and brackets_stack[-1] != brackets_match[c]:
                return False
            if not brackets_stack:
                return False
            else:
                brackets_stack.pop()
        else:
            brackets_stack.append(c)

    return len(brackets_stack) == 0
