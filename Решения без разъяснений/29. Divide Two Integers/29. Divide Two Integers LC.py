def my_solution1(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    sign = 0
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    rem = dividend
    quotient = 0
    while rem >= divisor:
        rem -= divisor
        quotient += 1
    if sign:
        return quotient - quotient - quotient
    return quotient