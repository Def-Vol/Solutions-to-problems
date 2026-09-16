def my_solution1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    try:
        return nums.index(target)
    except:
        nums.append(target)
        nums.sort()
        return nums.index(target)