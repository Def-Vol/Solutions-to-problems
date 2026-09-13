def my_solution1(s, words):
    if any(s.find(w) == -1 for w in words):
        return []
    if s.count(s[0]) == len(s):
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
