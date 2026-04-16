class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs)):
            res += str(len(strs[i]))
            res += "|"
            res += strs[i]

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            curr_sep = s.find("|", i)
            currWordLen = int(s[i:curr_sep])
            i = curr_sep + 1
            currWord = s[i:i + currWordLen]
            res.append(currWord)
            i = i + currWordLen

        return res




