def my_solution1(nums: list[int]):
    k = 0
    dupl = 1
    for n1 in range(1, len(nums)):
        if nums[k] != nums[n1]:
            k += 1
            dupl = 1
            nums[k] = nums[n1]
        elif dupl != 2:
            k += 1
            nums[k] = nums[n1]
            dupl = 2
    del nums[k+1:]
    return k+1