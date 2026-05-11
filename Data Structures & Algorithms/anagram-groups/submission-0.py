class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        indices = {}
        groups = {}

        for i, val in enumerate(strs):
            indices[i] = val

            s = "".join(sorted(val))

            if s not in groups:
                groups[s] = [i]
            else:
                temp = groups[s]
                temp.append(i)
                groups[s] = temp

        sol = []
        for key, val in groups.items():
            arr = [strs[i] for i in val]
            sol.append(arr)

        return sol