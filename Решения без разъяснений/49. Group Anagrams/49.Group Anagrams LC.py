def my_solution1(strs: list[str]):
    words = {}
    for word in strs:
        anagr = tuple(sorted(word))   #str(list(word).sort())
        if anagr in words:
            words[anagr].append(word)
        else:
            words[anagr] = [word]
    return list(words.values())