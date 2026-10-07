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
        concats = words[1:]
        if left not in result and left >= 0:
            leftw = s[left:n1]
        if n1 + leng*2 <= lens:
            rightw = s[right:right+leng]
        while leftw in concats:
            concats.remove(leftw)
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
            if left >= 0 and left not in result:
                result.append(left)
            else:
                result.append(n1)
    return result


'''
Мне не нужен словарь - достаточно списка индексов любого слова из words, так как
любая конкатенированная строка должна содержать все слова из списка.
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


#Это решение выполняет задачу частично: пройденных тестов 163 из 183
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
