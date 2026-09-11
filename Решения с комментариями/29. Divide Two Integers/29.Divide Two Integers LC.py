#Моё самое простое решение, главный недостаток которого это длительное время исполнения.
#При колоссальной разнице в значениях делимого и делителя количество итераций цикла будет слишком большим
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


#Второе моё решение, которое не имеет проблемы предыдущего, так как выполняет разницу с отдельными цифрами
#числа, а не со всем числом. По сути это алгоритмическая реализация деления в столбик из школьной программы
def my_solution2(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    #Несколько условий для тех входных значений, которые дают очевидное частное
    if dividend == divisor:
        return 1
    if dividend == 0:
        return 0
    if divisor == -1 and dividend < 0:  
        return abs(dividend)-1
    #Создаём флаговую переменную, определяющую знак, ибо входные значения могут быть в том числе отрицательными
    sign = 0
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    #Поскольку флаговая переменная определена, дальше можем спокойно работать только с положительными значениями
    dividend = abs(dividend)
    divisor = abs(divisor)
    #Ещё одно условие для очевидного частного: когда делитель = 1, то делимое равняется частному
    if divisor == 1:
        if sign:
            return dividend - dividend - dividend
        return dividend
    #Наконец начинаем "делить в столбик"
    dividend = str(dividend)    #Цикл должен работать со строкой, чтобы мы могли брать несколько цифр отдельно от всего числа
    divd = None    #Та самая переменная, которой и будут присваиваться несколько цифр из делимого
    divs = divisor    #Делитель будет всегда один и тот же
    res = ''    #Переменная, накапливающая результат (частное). При "делении" divd на divs полученную цифру(-ы) мы должны каждый раз записывать в результат слева-направо
    factor = 0     #Поскольку само деление у нас под запретом, то factor будет считать сколько раз мы отняли divs от divd
    exten = 0     #Переменная, считающая сколько раз мы нарастили divd, прежде чем он бы стал больше divs, чтобы выполнить деление
    for n1 in dividend:
        if divd is not None:    #Если после предыдущего "деления", в divd сохранился остаток, то он сохраняет его, а следущее переносимое из делимого число ставится в конец
            divd += n1
        else:   
            if n1 == '0':   #Если после предыдущего "деления", divd "поделился" без остатка, а следующее число в делимом это ноль, то просто переносим его сразу в результат
                res += '0'
                continue
            divd = n1   #Если divd пустой, то просто приравниваем его к следующему числу, переносимому из делимого
        if factor:     #Наращивание divd ПОЛНОСТЬЮ "беслатно" при его первом создании, поэтому "платным режим" включаем только для последующих созданий divd
            exten += 1
            if exten > 1:   #Одно из правил деления в столбик: одно число для divd переносится "бесплатно", в вот при каждом следующем наращивании divd, необходимо добавлять ноль в результат
                res += '0'
        if int(divd) < divs:    #Проверяем, достаточно ли нарастили divd для его деления на делитель, если нет -> повторить предыдущий код
            continue
        divd = int(divd)    #Для выполнения математических операций divd не должен быть строкой
        factor = 0     #Откатываем накопитель для нового divd
        while divd >= divs:    #Выполняем "деление", то есть сколько раз делитель помещается в делимом, а для этого просто выполняем разницу
            divd -= divs
            factor += 1
        exten = 0    #Поскольку текущий divd мы уже "поделили" и будем создавать новый, то и счётчик наращивания следует откатить до ноля
        if factor:
            res += str(factor)
        if divd == 0:
            divd = None
        else:
            divd = str(divd)
    if exten and divd:     #Если последняя итерация цикла завершилась на строчке if int(divd) < divs: , нужно добавить последний 0
        res += '0'
    res = int(res) if res else 0
    if sign:    #Если результат должен быть отрицательным, то просто отнимаем его от самого себя два раза
        return res - res - res    #Альтернатива: ~res + 1
    return res