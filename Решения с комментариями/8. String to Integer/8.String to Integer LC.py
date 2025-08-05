#https://leetcode.com/problems/string-to-integer-atoi/description/ - условие задачи



'''
Сначала избавляю строку от всех ведущих и замыкающих пробельных символов. После
чего сразу возвращаю ноль, если длина строки меньше или равна 1. Если нет,
сохраняю знак, удалив его, и снова выполняю проверку, но только первого символа,
так как по условию надо вернуть только цифры до первого нецифрового символа.
Далее при помощи цикла получаю индекс первого такого символа, чтобы получить
срез цифр из строки.
'''
def mySolution(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    sign = 1
    if len(s) <= 1 and not s.isdigit():
        return 0
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    if not s[0].isdigit():
        return 0
    alpha = len(s)
    for i in range(len(s)):
        if not s[i].isdigit():
            alpha = i
            break
    num = int(s[:alpha]) * sign
    if -2**31 <= num <= 2**31-1:
        return num
    elif num < -2**31:
        return -2**31
    else:
        return 2**31-1
