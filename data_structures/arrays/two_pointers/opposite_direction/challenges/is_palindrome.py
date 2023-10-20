def is_palindrome(s: str) -> bool:
    s = [c.lower() for c in s if c.isalnum()]
    n = len(s)
    if n == 0:
        return True

    left, right = 0, n - 1

    while left <= right:
        left_char = s[left].lower()
        right_char = s[right].lower()

        if left_char != right_char:
            return False

        left += 1
        right -= 1

    return True
