class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c_s = {}
        c_t = {}

        for i in range(len(s)):
            count = c_s.get(s[i], 0) + 1
            c_s[s[i]] = count + 1

            count = c_t.get(t[i], 0) + 1
            c_t[t[i]] = count + 1

        return c_s == c_t