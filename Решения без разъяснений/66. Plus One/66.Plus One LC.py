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


def my_solution2(digits):
    num = -1
    rem = 0
    end = len(digits)-1
    for i in range(end, -1, -1):
        if rem == 1:
            num = digits.pop(i)
            num += 1
            rem = 0
        if i == end:
            num = digits.pop(i)
            num += 1
        if num == 10:
            rem = 1
            num = 0
        if num != -1:
            digits.insert(i, num)
            num = -1
    if rem == 1:
        digits.insert(0, 1)
    return digits
