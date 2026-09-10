def my_solution1(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == divisor:
        return 1
    if dividend == 0:
        return 0
    if divisor == -1 and dividend < 0: 
        return abs(dividend)-1
    sign = 0
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    if divisor == 1:
        if sign:
            return dividend - dividend - dividend
        return dividend
    rem = dividend
    quotient = 0
    while rem >= divisor:
        rem -= divisor
        quotient += 1
    if sign:
        return quotient - quotient - quotient
    return quotient


def my_solution2(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == divisor:
        return 1
    if dividend == 0:
        return 0
    if divisor == -1 and dividend < 0:  
        return abs(dividend)-1
    sign = 0
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    if divisor == 1:
        if sign:
            return dividend - dividend - dividend
        return dividend
    dividend = str(dividend)
    divd = None
    divs = divisor
    res = ''
    factor = 0
    exten = 0
    for n1 in range(len(dividend)):
        if divd is not None:
            divd += dividend[n1]
        else:
            if dividend[n1] == '0':
                res += '0'
                continue
            divd = dividend[n1]
        if factor:
            exten += 1
            if exten > 1:
                res += '0'
        if int(divd) < divs:
            continue
        divd = int(divd)
        factor = 0
        while divd >= divs:
            divd -= divs
            factor += 1
        exten = 0
        if factor:
            res += str(factor)
        if divd == 0:
            divd = None
        else:
            divd = str(divd)
    if exten and divd:
        res += '0'
    res = int(res) if res else 0
    if sign:
        return res - res - res
    return res