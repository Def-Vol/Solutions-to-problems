#"remove the duplicates in-place", то есть суть задачи: удалять повторяющиеся значения необходимо именно в переданном списке, не создавая новый
def my_solution1(nums): 
    """
    :type nums: List[int]
    :rtype: int
    """
    ind = 0
    while ind < len(nums):
        rcount = nums.count(nums[ind])
        if rcount > 1:
            for n1 in range(rcount-1):
                nums.remove(nums[ind])
        ind += 1