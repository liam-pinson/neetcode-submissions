class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_sorted = sorted(s1)
        print(len(s2) - len(s1))
        for i in range(len(s2) - len(s1) + 1):
            substr = s2[i:i+len(s1)]
            print(substr)
            s2_sorted = sorted(substr)
            if s1_sorted == s2_sorted:
                return True

        return False