'''
Необычный график времени исполнения (Runtime) моего финального решения (my_solution6()) 
объясняется тем, что подавляющее большинство участников портала не смогли решить задачу
и просто копировали в проверку готовое решение портала из раздела Solutions, которое,
конечно, самое быстрое. Так что самостоятельные решения участников представлены
маленькими столбиками, которые в сумме дают чуть более 10%. То есть самостоятельно
решить эту задачу смог только каждый десятый.
'''




#---!!!Просматривать этот файл стоит снизу вверх, если необходимо проследить последовательность этапов получения автором финального решения. Все комментарии, кроме концевых, так же следует читать по восходящей.
'''
Моё законченное решение (my_solution6()), полностью выполняющее задачу. В завершение можно 
избавить код от переменной lconc, которая используется в итоге всего один раз, поэтому 
скорость выполнения она не увеличивает вовсе, даже наоборот, ибо на выполнение инструкции 
присваивания так же расходуется время, но главное, удалив переменную, уменьшим объём 
используемой оперативной памяти, хоть и не намного.

Пока писал комментарии для этой функции, заметил, что её код можно улучшить в тех случаях,
когда берутся индексы не дубликатов, а того слова, которое в words встречается единожды,
в то время как дубликаты в words имеются. Потому что в таких случаях появляются лишние
итерации внешнего цикла, когда в конце полученный (в результате всей итерации) индекс 
конкатенированной строки просто отсеивается, потому что он уже есть в результирующем 
списке. Чтобы избавится от этих лишних огромных итераций, можно попробовать брать индексы
только самого часто встречающегося в words слова или вовсе обращаться с дубликатами как-то 
иначе. Я уже не буду тратить время на это улучшение, так как моё решение всё равно опередило 
по скорости более 90% самостоятельных решений других участников портала.
'''
def my_solution6(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    for w in set(words):    #Сразу отсеиваем те входные данные, где нет какого-либо слова в строке
        if w not in s:
            return []
    leng = len(w)
    lens = len(s)
    if leng*len(words) > lens:  #Теперь отсеиваем те, где общая длина конкатенированной больше всей строки (потому что предыдущий цикл не учитывает дубликаты в words)
        return []
    result = []
    inds = []
    word = words[0]
    ind = s.find(word)
    while ind != -1:    #Получаем список индексов любого слова из words (хоть первого). Список вхождений, иными словами. Почему обходим в цикле именно подобный список, я написал ранее (над функцией my_solution4)
        inds.append(ind)
        ind = s.find(word, ind + 1)
    for n1 in inds:     #Запускаем главный цикл
        left = n1 - leng    #Посколько остальные конкатенированные слова могут находиться как слева, так и справа от вхождения, нужно работать с обеими сторонами вхождения. 
        right = n1 + leng    #left и right - индекс левого возможного слова из words и индекс правого возможного слова из words
        leftw = ''    #Эти переменные нужны для хранения проверяемых строк
        rightw = ''
        left_ind = False    #Булевые переменные, устанавливающие флаг: было найдено хотя бы одно слово из words слева и хотя бы одно справа?
        right_ind = False
        concats = words[1:]     #Список, хранящий оставшиеся слова из words - из него будем удалять слова, которые окажутся равны строкам справа и слева от вхождения. Соответственно, если этот список опустеет, это будет главным маркером индентификации конкатенированной строки. Так что фактически этот список - небулевая флаговая переменная
        if left not in result and left >= 0:    #Поскольку left может являться началом конкатенированной строки, которое будем добавлять в результирующий список, следует проверить нет ли его уже в этом списке.
            leftw = s[left:n1]      #Получаем строку слева для проверки 
        if right + leng <= lens:
            rightw = s[right:right+leng]    #Получаем строку справа для проверки 
        while leftw in concats:     #Вложенный цикл для проверки левых строк, где каждая итерация приближается к началу строки s
            concats.remove(leftw)
            left_ind = True
            if not concats:     #Если после последнего удаления в concats ничего не осталось, то мы уже получили индекс конкатенированной строки
                break
            left -= leng    #Если concats не пустой, то идём дальше влево, пока наконец concats не опустеет или следующая левая подстрока не окажется словом из words
            if left >= 0:
                leftw = s[left:left+leng]   #Соответственно получаем следующую левую подстроку для проверки
            else:
                break    #Если следующий левый взятый индекс оказался ниже ноля, то цикл достиг начала строки s и искать дальше слева фактически нечего
        if left_ind and concats:    #Предыдущий цикл может завершится аж в трёх местах, поэтому после него left может ссылаться уже не начало индентифицируемой конкатенированной строки, а на более ранний индекс. Это необходимо исправить, потому что left может пойти в результат.
            left += leng
            leftw = s[left:left+leng]
        while rightw in concats:    #Теперь проверяем подстроки справа от вхождения
            concats.remove(rightw)
            right_ind = True
            '''
            В ситуациях, когда words содержит дубликаты, а конкатенированная строка соответственно состоит из этих повторений, 
            в списке индексов могут содержатся индексы (тогда, когда это индексы именно продублированного слова), обходить которые
            уже не будет смысла, потому что в следующей итерации left будет ссылаться на ту же конкатенированную строку
            которую получили в предыдущей итерации внешнего цикла, и полученный индекс в итоге просто отсеится и при чём произойдёт
            это только в конце итерации внешнего цикла. Поэтому из списка вхождений inds стоит удалить эти индексы дубликатов 
            (что и происходит в следующих двух строчках кода) - так мы избавимся в некоторых случаях от огромного количества ненужных 
            итераций внешнего цикла, что во много раз ускорит исполнение этого кода.
            '''
            if right in inds:   
                inds.remove(right)    
            if not concats:
                break
            right += leng
            if right + leng <= lens:
                rightw = s[right:right+leng]
            else:
                break
        if not concats:     #Если concats опустел, значит конкатенированная строка индентифицирована и индекс её начала можно добавлять в результат
            if left_ind:   
                if left not in result:
                    result.append(left)
                if right_ind:   #С этой строчки начинается код проверки одного вхождения на несколько конкатенированных строк, в которые слово (вхождения) может быть включено. Этот финальный участок кода я описал внизу, над функцией my_test5()
                    right += leng
                    rightw = s[right:right+leng]
                while rightw == leftw:
                    left += leng
                    leftw = s[left:left+leng]
                    result.append(left)
                    if left == n1:
                        break
                    right += leng
                    rightw = s[right:right+leng]
            else:
                result.append(n1)   #Если слева не было обнаружено ни одного слова words, а concats тем не менее опустела, то вхождение и есть начало всей конкатенированной строки
    return result


'''
Решение не проходило тест c s = "abaababbaba", words = ["ab","ba","ab","ba"]. В попытках разобраться, 
почему так происходит, я обнаружил лишнюю инструкцию left += leng в конце цикла while leftw in concats, 
которую оставил там ещё до написания конечного вложенного цикла while rightw == leftw, забыв про неё.
'''
def my_test6(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    print(f'{s}, {words}')
    for w in set(words):
        if w not in s:
            return []
    leng = len(w)
    lconc = leng*len(words)
    lens = len(s)
    if lconc > lens:
        return []
    result = []
    inds = []
    word = words[0]
    ind = s.find(word)
    while ind != -1:
        inds.append(ind)
        ind = s.find(word, ind + 1)
    print(f'word = {word}, inds = {inds}')
    for n1 in inds:
        print(f'n1 = {n1}')
        left = n1 - leng
        right = n1 + leng
        leftw = ''
        rightw = ''
        left_ind = False
        right_ind = False
        concats = words[1:]
        if left not in result and left >= 0:
            leftw = s[left:n1]
        if right + leng <= lens:
            rightw = s[right:right+leng]
        while leftw in concats:
            print(f'Л {left}: {leftw}')
            concats.remove(leftw)
            left_ind = True
            if not concats:
                break
            left -= leng
            if left >= 0:
                leftw = s[left:left+leng]
            else:
                break
        print(f'left = {left}')
        if left_ind and concats:
            left += leng
            leftw = s[left:left+leng]
        while rightw in concats:
            print(f'П {right}: {rightw}')
            concats.remove(rightw)
            right_ind = True
            if right in inds:
                print(f'Удалено: {right}')
                inds.remove(right)
            if not concats:
                break
            right += leng
            if right + leng <= lens:
                rightw = s[right:right+leng]
            else:
                break
        if not concats:
            if left_ind:
                if left not in result:
                    result.append(left)
                    print('Первый', left)
                if right_ind:
                    right += leng
                    rightw = s[right:right+leng]
                while rightw == leftw:
                    left += leng
                    leftw = s[left:left+leng]
                    print(f'Последующий: {left}')
                    result.append(left)
                    if left == n1:
                        break
                    right += leng
                    rightw = s[right:right+leng]
            else:
                result.append(n1)
        print(f'Результат: {result}')
    return result
print(my_test6("abaababbaba", ["ab","ba","ab","ba"]))


''' 
Далее для доработок мне пришлось добавить функции print(), чтобы во время тестов легко находить места 
в коде, где переменные получают плохие данные или теряют хорошие.

Чтобы находить все конкатенированные строки на одно вхождение, я добавил в конце цикл while rightw == leftw,
исполняющийся уже после индентификации конкатенированной строки. Поскольку моё решение гарантировано возращает
именно наименьший индекс этой строки в одном вхождении, то для идентификации остальных конкатенированных строк
в этом же вхождении достаточно получить индекс второго слова индентифицированной и проверить является ли первое
слово равно подстроке той же длины, идущей сразу после конкатенированной и если да, то это гарантированно ещё
одна конкатенированная строка в этом вхождении, потому что забрав одно слово в начале, именно этого одного слова 
не хватает для полной конкатенированной строки. Остальные же случаи (когда второе слово идёт сразу после первой
идентифицированной конкатенированной строки, а потому уже первое) обнаружится при чтении следующих вхождений, 
то есть следующих итераций внешнего цикла for n1 in inds. Таким образом мы находим все конкатенированные строки 
в одном вхождении. 
'''
def my_test5(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    print(f'{s}, {words}')
    for w in set(words):
        if w not in s:
            return []
    leng = len(w)
    lconc = leng*len(words)
    lens = len(s)
    if lconc > lens:
        return []
    result = []
    inds = []
    word = words[0]
    ind = s.find(word)
    while ind != -1:
        inds.append(ind)
        ind = s.find(word, ind + 1)
    print(inds)
    for n1 in inds:
        left = n1 - leng
        right = n1 + leng
        leftw = ''
        rightw = ''
        left_ind = False
        right_ind = False
        concats = words[1:]
        if left not in result and left >= 0:
            leftw = s[left:n1]
        if right + leng <= lens:
            rightw = s[right:right+leng]
        while leftw in concats:
            print(f'Л {left}: {leftw}')
            concats.remove(leftw)
            left_ind = True
            if not concats:
                break
            left -= leng
            if left >= 0:
                leftw = s[left:left+leng]
            else:
                left += leng
                break
        print(left)
        if left_ind and concats:
            left += leng
            leftw = s[left:left+leng]
        while rightw in concats:
            print(f'П {right}: {rightw}')
            concats.remove(rightw)
            right_ind = True
            if right in inds:
                inds.remove(right)
                print(f'Удалено: {right}')
            if not concats:
                break
            right += leng
            if right + leng <= lens:
                rightw = s[right:right+leng]
            else:
                break
        if not concats:
            if left_ind:
                if left not in result:
                    result.append(left)
                    print('Первый', left)
                if right_ind:
                    right += leng
                    rightw = s[right:right+leng]
                while rightw == leftw:
                    left += leng
                    leftw = s[left:left+leng]
                    result.append(left)
                    if left == n1:
                        break
                    right += leng
                    rightw = s[right:right+leng]
            else:
                result.append(n1)
        print(f'Результат: {result}')
    return result
#print(my_test5('barfoofoobarthefoobarman', ["bar","foo","the"]))
#print(my_test5("bcabbcaabbccacacbabccacaababcbb", ["c","b","a","c","a","a","a","b","c"]))


'''
Это решение не проходит даже тест с barfoofoobarthefoobarman' и ["bar","foo","the"]. Всё из-за того, что
по каждому вхождению идентифицируется только одна конкатенированная строка, тогда как их может быть 
несколько на одно вхождение. Для исправления я добавил ещё один вложенный цикл - смотрите следующее решение 
выше.
'''
def my_solution5(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    for w in set(words):
        if w not in s:
            return []
    leng = len(w)
    lconc = leng*len(words)
    lens = len(s)
    if lconc > lens:
        return []
    result = []
    inds = []
    word = words[0]
    ind = s.find(word)
    while ind != -1:
        inds.append(ind)
        ind = s.find(word, ind + 1)
    for n1 in inds:
        left = n1 - leng
        right = n1 + leng
        leftw = ''
        rightw = ''
        left_ind = False
        concats = words[1:]
        if left not in result and left >= 0:
            leftw = s[left:n1]
        if right + leng <= lens:
            rightw = s[right:right+leng]
        while leftw in concats:
            concats.remove(leftw)
            left_ind = True
            if not concats:
                break
            left -= leng
            if left >= 0:
                leftw = s[left:left+leng]
            else:
                break
        while rightw in concats:
            concats.remove(rightw)
            if right in inds:
                inds.remove(right)
            if not concats:
                break
            right += leng
            if right + leng <= lens:
                rightw = s[right:right+leng]
            else:
                break
        if not concats:
            if left_ind:
                result.append(left)
            else:
                result.append(n1)
    return result


'''
Мне не нужен словарь - достаточно списка индексов любого слова из words, так как
любая конкатенированная строка должна содержать все слова из списка.

Когда я писал это решение, дойдя до момента, где надо было решить, какими циклами
обходить списки индексов из словаря, меня осенило: мне нужен только один такой список
с индексами любого слова из words - ВСЁ! Вот он - главный цикл (тот который обходит
этот список), от него надо плясать, ОН способен содержать весь код решения с поиском
всех конкатенированных строк. В дальнейших решениях (выше) я уже был убеждён, что
иду верной дорогой.
'''
def my_solution4(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    for w in set(words):
        if w not in s:
            return []
    leng = len(w)
    lconc = leng*len(words)
    lens = len(s)
    if lconc > lens:
        return []
    result = []
    start = 0
    inds = []
    iwords = {}
    for w1 in words:
        ind = s.find(w1, start)
        while ind != -1:
            inds.append(ind)
            ind = s.find(w1, ind + 1)
        iwords[w1] = inds
        inds = []
    left = None
    right = None
    for n in iwords[w1]:
        if left == None:
            left = n - leng
        if right == None:
            right = n + leng
        concat = True
        for w2 in iwords:
            if w2 == w1:
                continue
            #if left not in 

        pass
            
'''
ИЗМЕНЕНИЕ ТРАЕКТОРИИ ПОИСКА РЕШЕНИЯ

Мои прошлые попытки (внизу) я счёл несостоявшимися, ибо нужны другие циклы. Всё время пока
я писал те решения, меня не отпускали мысли, что циклы определённо неудачные. Даже
если и получится при помощи них получить окончательное решение, то время исполнения
кода будет колоссальным, что в итоге меня отвадило продолжать работать с ними. Дальше
я начал думать о словаре, как о единственном варианте решения. Словарь, где ключи это
строки из words, а значения это списки их индексов во входящей строке. Казалось, 
написать решение с разумным временем исполнения можно только с таким словарём, хотя я
до последнего не хотел использовать эту структуру, ибо работа с ней почти всегда 
гарантирует большое время исполнения и огромный объём занимаемой оперативной памяти.
'''


'''
Мысль: ведь конкатенированная строка это последовательность индексов строк, с разницей в длину одной строки. 
Может, получится найти минимальный индекс возможной конкатенированной строки и выполнить проверку наоборот:
не слова искать в строке, а создать список индексов на основе начального индекса и количества строк в words, 
а потом проверять, соответствуют ли эти индексы строкам?
'''


'''
В попытках найти простое решение для решения теста 157 (подробнее после функции). Я решил добавить дополнительное
условие после прохождения if ind == -1 or ind + leng > lens, так как именно оно в итоге возращает пустой список.
Это условие: если минимальный полученный индекс всё ещё допускает наличие конкатенированной строки, то всего лишь
изменить значение start и начать поиск строки сначала. Однако это не позволило получить верное решение банально из-за
того, что цикл for всегда начинает поиск именно с определённого слова, тогда как для получения верного решения в этом
тесте необходимо начинать поиск с другого, либо при нахождения слова не штриховать строку.
'''
def my_solution3(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    for w in set(words):
        if w not in s:
            return []
    leng = len(w)
    lconc = leng*len(words)
    lens = len(s)
    if lconc > lens:
        return []
    result = []
    start = 0
    while start < lens:
        inds = []
        while len(inds) < len(words):
            inds = []
            string = s
            for w in words:
                ind = string.find(w, start)
                print(w)
                if ind == -1 or ind + leng > lens:
                    if inds and min(inds) + 1 + lconc <= lens:
                        start = min(inds) + 1
                        break
                    else:
                        print(w)
                        print(inds)
                        return result
                string = string[:ind] + '*'*leng + string[ind+leng:]
                inds.append(ind)
        inds.sort()
        print(inds)
        num = None
        concat = True
        for n in inds:
            if not num:
                num = n
                continue
            if n - num != leng:
                concat = False
                print(f'{n}-{num}!={leng}')
                print('НЕТ')
                break
            num = n
        if concat:
            result.append(inds[0])
            print('ДА')
        start = inds[0] + 1
    return result

'''
Это решение выполняет задачу частично: пройденных тестов 156 из 183. При входных данных s = "ababaab", 
words = ["ab","ba","ba"] решение выдаёт пустой список, тогда как результат должен быть = [1]. В поисках
решения я решил добавить ещё один вложенный цикл while на уровне вложенности между while start < len(s) 
и for w in words - смотрите my_solution3() выше.
'''
def my_solution2(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    for w in set(words):
        if w not in s:
            return []
    leng = len(w)
    if leng*len(words) > len(s):
        return []
    result = []
    start = 0
    while start < len(s):
        inds = []
        string = s
        for w in words:
            ind = string.find(w, start)
            if ind == -1 or ind + leng > len(string):
                return result
            string = string[:ind] + '*'*leng + string[ind+leng:]
            inds.append(ind)
        inds.sort()
        num = None
        concat = True
        for n in inds:
            if not num:
                num = n
                continue
            if n - num != leng:
                concat = False
                break
            num = n
        if concat:
            result.append(inds[0])
        start = inds[0] + 1
    return result

#Это решение выполняет задачу частично: пройденных тестов 163 из 183.
#Это решение старое - создавалось неделю или две назад от момента, как я снова вернулся к этой задаче. Поэтому новые решения (выше) я писал с читого листа, без оглядки на это
def my_solution1(s, words):
    if any(s.find(w) == -1 for w in words):
        return []
    if len(set(s)) == 1:
        last = len(s) - len(words[0])*len(words)
        return [ind for ind in range(len(s)) if ind <= last]
    ns = s
    result = []
    if len(words) == 1:
        word = words[0]
        let = len(word)
        fir = ns.find(word)
        while fir != -1:
            result.append(fir)
            ns = ns.replace(word, '^'*let, 1)
            fir = ns.find(word)
        return result
    concat = {}
    start_ind = []
    remw = []
    finish = False
    while not finish:
        if not remw:
            remw = words[:]
        for n1 in remw:
            ind = ns.find(n1)
            if ind == -1:
                finish = True
                break
            concat[ind] = n1
            start_ind.append(ind)
            ns = ns.replace(n1, '^'*len(n1), 1)
        if finish:
            break
        start_ind.sort()
        #first = len(start_ind) - len(remw) - 1 if len(start_ind) > len(remw) else 0
        after = start_ind[0] + len(concat[start_ind[0]])
        res = True
        for n2 in range(1, len(start_ind)):
            num = start_ind[n2]
            if after != num:
                res = False
                last = n2 
                break
            after = num + len(concat[num])
        if res:
            result.append(start_ind[0])
            remw = [concat[start_ind[0]]]
            start_ind = start_ind[1:]
        else:
            remw = [concat[s1] for s1 in start_ind[:last]]
            if len(remw) > 1 and any(ns.find(n4, start_ind[last-1]) != -1 for n4 in remw):
                last = last-1
                del remw[-1]
            start_ind = start_ind[last:]
    return result