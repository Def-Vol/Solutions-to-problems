def mySolution(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = strs[0]
        for w in strs:
            if w == '' or w[0] != pref[0]:
                return ''
            if w.find(pref) != 0:
                for li in range(len(pref)):
                    if li == len(w) or w[li] != pref[li]:
                        pref = pref[:li]
                        break
        return pref
