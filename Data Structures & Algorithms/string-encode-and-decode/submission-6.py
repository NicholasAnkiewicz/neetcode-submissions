class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0:
            return "[]"
        for s in strs:
            res = res + 'µ' + s
        print(res[1:])
        return res[1:]
    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        res = []
        new_s = ""
        for c in s:
            if c == 'µ':
                print(new_s)
                res.append(new_s)
                new_s = ""
            else:
                new_s += c
        res.append(new_s)
        return res