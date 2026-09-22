def my_solution1(s):
    """
    :type s: str
    :rtype: int
    """
    rs = s[::-1].strip()
    if ' ' in rs:
        return rs.index(' ')
    else:
        return len(rs)


def my_solution2(s):
    if ' ' in s:
        return len(s.split()[-1])
    else:
        return len(s)