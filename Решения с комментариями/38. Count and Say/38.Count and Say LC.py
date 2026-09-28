def my_solution1(n):
    """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        result = '11'
        n -= 2
        for n1 in range(n):
            string = result
            letters = result[0]
            result = ''
            for n2 in range(1, len(string)):
                if string[n2] != letters[0]:
                    result = result + str(len(letters)) + letters[0]
                    letters = ''
                letters += string[n2]
            result = result + str(len(letters)) + letters[0]
        return result
