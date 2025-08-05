def mySolution(s):
        num = 0
        for r in range(len(s)):
            if s[r] == 'M':
                if r == 0 or s[r-1] != 'C':
                    num += 1000
                else:
                    num += 900
            elif s[r] == 'D':
                if r == 0 or s[r-1] != 'C':
                    num += 500
                else:
                    num += 400
            elif s[r] == 'C':
                if r != 0 and s[r-1] == 'X':
                    num += 90
                elif r == len(s)-1 or (s[r+1] != 'D' and s[r+1] != 'M'):
                    num += 100
            elif s[r] == 'L':
                if r == 0 or s[r-1] != 'X':
                    num += 50
                else:
                    num += 40
            elif s[r] == 'X':
                if r != 0 and s[r-1] == 'I':
                    num += 9
                elif r == len(s)-1 or s[r+1] != 'L' and s[r+1] != 'C':
                    num += 10
            elif s[r] == 'V':
                if r == 0 or s[r-1] != 'I':
                    num += 5
                else:
                    num += 4
            else:
                if r == len(s)-1 or (s[r+1] != 'V' and s[r+1] != 'X'):
                    num += 1
        return num
