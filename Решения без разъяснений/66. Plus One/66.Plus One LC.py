def my_solution1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = 0
    rem = 0
    result = []
    for i in range(len(digits)-1, -1, -1):
        num = digits[i]
        if rem == 1:
            num += 1
            rem = 0
        if i == len(digits)-1:
            num += 1
        if num == 10:
            rem = 1
            num = 0
        result.append(num)
    if rem == 1:
        result.append(rem)
    result.reverse()
    return result