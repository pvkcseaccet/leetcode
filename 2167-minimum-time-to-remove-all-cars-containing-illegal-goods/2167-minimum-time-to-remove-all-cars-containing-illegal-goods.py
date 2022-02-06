class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pref, suff = [0 for i in range(n)], [0 for i in range(n)]
        pref[0], suff[n-1] = int(s[0]), int(s[n-1])
        for i in range(1,n): pref[i] = min(i+1, pref[i-1]+2) if s[i] == '1' else pref[i-1]
        for i in range(n-2, -1, -1): suff[i] = min(n-i, suff[i+1]+2) if s[i] == '1' else suff[i+1]
        cost = min(pref[n-1], suff[0])
        for i in range(n-1): cost = min(cost, pref[i]+suff[i+1])
        return cost