def decode_ways(digits):
    # Memoization dictionary to store the number of ways to decode for each starting index
    memo = {}

    def dfs(start_index):
        nonlocal memo
        # Check memoization dictionary for a previously computed result
        if start_index in memo:
            return memo[start_index]

        # Base case: Reached the end of the string, so there's only one way to decode (doing nothing)
        if start_index == len(digits):
            return 1

        # Initialize variable to keep track of the number of ways to decode from the current index
        ways = 0

        # Special case: can't decode string with a leading '0'
        if digits[start_index] == '0':
            return 0  # No way to decode

        # Option 1: Decode the next single digit
        ways += dfs(start_index + 1)

        # Option 2: Decode the next two digits, if valid
        if start_index < len(digits) - 1:  # Make sure we don't go out of bounds
            double_digit = int(digits[start_index:start_index + 2])
            if 10 <= double_digit <= 26:  # Check if the two digits form a valid number for decoding
                ways += dfs(start_index + 2)

        # Save the computed result in the memoization dictionary
        memo[start_index] = ways

        return ways

    return dfs(0)
