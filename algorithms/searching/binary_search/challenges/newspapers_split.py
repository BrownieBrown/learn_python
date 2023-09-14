from typing import List


def feasible(newspapers_read_times: List[int], num_coworkers: int, limit: int) -> bool:
    # time to keep track of the current worker's time spent, num_workers to keep track of the number of coworkers used
    time, num_workers = 0, 0
    for read_time in newspapers_read_times:
        # check if current time exceeds the given time limit
        if time + read_time > limit:
            time = 0
            num_workers += 1
        time += read_time
    # edge case to check if we needed an extra worker at the end
    if time != 0:
        num_workers += 1
    # check if the number of workers we need is more than what we have
    return num_workers <= num_coworkers


def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    result = -1
    while low <= high:
        mid = (low + high) // 2
        # helper function to check if a time works
        if feasible(newspapers_read_times, num_coworkers, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


"""
feasible function:
This function checks if it's possible to split the newspapers among the given number of coworkers such that no coworker reads for more than limit time.

You initialize the time (time taken by current coworker) and num_workers (number of coworkers currently assigned) to 0.
For each newspaper read time, if the time taken by the current coworker plus this read time exceeds the limit, you reset the time to 0 and increment the number of coworkers.
Otherwise, you just add the read time to the current coworker's time.
After the loop, you check if there's still some time left for the last coworker (i.e., the current coworker hasn't reached the limit). If so, you increment the number of coworkers.
Finally, you check if the number of coworkers you've used is less than or equal to the given num_coworkers.
newspapers_split function:
This is a binary search function that tries to find the minimum maximum reading time.

The search space is between the maximum read time (a single coworker reading the newspaper that takes the most time) and the total read time (a single coworker reading all newspapers). This sets your initial low and high.
Using binary search, you find the mid-point and check if this mid-point time is feasible using the feasible function.
If it's feasible, you've found a potential answer (ans). But you continue the search in the lower half (trying to minimize the time).
If it's not feasible, you need to increase the time, so you search in the upper half.
Finally, you return ans which will have the minimum maximum reading time.
"""
