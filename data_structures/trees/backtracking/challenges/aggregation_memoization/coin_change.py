from typing import List


def coin_change_memoization(coins: List[int], amount: int) -> int:
    memo = {}  # Memoization dictionary

    def dfs(remaining):
        # Check memoization
        if remaining in memo:
            return memo[remaining]

        # Base cases
        if remaining == 0:
            return 0
        if remaining < 0:
            return -1

        # Initialize minimum number of coins needed
        min_coins = float('inf')

        for coin in coins:
            res = dfs(remaining - coin)
            if res >= 0:
                min_coins = min(min_coins, 1 + res)

        # Save result to memo and return
        memo[remaining] = -1 if min_coins == float('inf') else min_coins
        return memo[remaining]

    return dfs(amount)


def coin_change(coins: List[int], amount: int) -> int:
    # Define the DFS function
    def dfs(remaining):
        # Base Case: If the remaining amount is 0, then no more coins are needed
        if remaining == 0:
            return 0

        # Base Case: If the remaining amount is negative, then no solution exists
        if remaining < 0:
            return -1

        # Initialize the minimum number of coins to be infinite
        min_coins = float('inf')

        # Try each coin
        for coin in coins:
            # Get the result of using this coin in the solution
            res = dfs(remaining - coin)

            # If a solution exists (res != -1), update the minimum number of coins
            if res >= 0:
                min_coins = min(min_coins, 1 + res)

        # Return -1 if no solution exists, otherwise return the minimum number of coins needed
        return -1 if min_coins == float('inf') else min_coins

    return dfs(amount)
