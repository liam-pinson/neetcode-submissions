class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for s in strs:
            encoded_string += (s + ".")

        return encoded_string

    def decode(self, s: str) -> List[str]:

        strs = s.split(".")

        return strs[:len(strs) - 1]
