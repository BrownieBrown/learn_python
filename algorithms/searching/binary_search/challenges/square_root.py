def square_root(n: int) -> int:
    if n == 0:
        return 0
    left, right, result = 1, n, -1

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result - 1
