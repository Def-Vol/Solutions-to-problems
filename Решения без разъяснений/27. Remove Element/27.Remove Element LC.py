def my_solution1(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while val in nums:
        nums.remove(val)