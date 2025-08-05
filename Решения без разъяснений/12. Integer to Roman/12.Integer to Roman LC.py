def mySolution(num):
        count = 1
        roman = ''
        while num != 0:
            rem = num % 10
            num //= 10
            if rem != 0:
                if rem == 1:
                    if count == 1:
                        roman += 'I'
                    if count == 2:
                        roman += 'X'
                    if count == 3:
                        roman += 'C'
                    if count == 4:
                        roman += 'M'
                if rem == 2:
                    if count == 1:
                        roman += 'II'
                    if count == 2:
                        roman += 'XX'
                    if count == 3:
                        roman += 'CC'
                    if count == 4:
                        roman += 'MM'
                if rem == 3:
                    if count == 1:
                        roman += 'III'
                    if count == 2:
                        roman += 'XXX'
                    if count == 3:
                        roman += 'CCC'
                    if count == 4:
                        roman += 'MMM'
                if rem == 4:
                    if count == 1:
                        roman += 'VI'
                    if count == 2:
                        roman += 'LX'
                    if count == 3:
                        roman += 'DC'
                if rem == 5:
                    if count == 1:
                        roman += 'V'
                    if count == 2:
                        roman += 'L'
                    if count == 3:
                        roman += 'D'
                if rem == 6:
                    if count == 1:
                        roman += 'IV'
                    if count == 2:
                        roman += 'XL'
                    if count == 3:
                        roman += 'CD'
                if rem == 7:
                    if count == 1:
                        roman += 'IIV'
                    if count == 2:
                        roman += 'XXL'
                    if count == 3:
                        roman += 'CCD'
                if rem == 8:
                    if count == 1:
                        roman += 'IIIV'
                    if count == 2:
                        roman += 'XXXL'
                    if count == 3:
                        roman += 'CCCD'
                if rem == 9:
                    if count == 1:
                        roman += 'XI'
                    if count == 2:
                        roman += 'CX'
                    if count == 3:
                        roman += 'MC'
            count += 1
        return roman[::-1]
