class Solution:
    #Take a window, 
    #move right if invalid 
    #move left if valid
    #Maintain/check shortest valid substring 
    #Check valid using frequency dictionary
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        T_dic = {}
        for c in t:
            T_dic[c] = 1 + T_dic.get(c, 0)
        left = 0
        res = ""
        resLen = float("infinity") 
        have = 0
        need = len(T_dic)

        for right in range(0, len(s)):    
            ch = s[right]
            window[ch] = 1 + window.get(ch, 0)
            if ch in T_dic and T_dic[ch] == window[ch]:
                have += 1
            while have == need:
                if right-left+1 < resLen:
                    res = [left,right]
                    resLen = right-left+1
                window[s[left]] -= 1  
                if s[left] in T_dic and window[s[left]] < T_dic[s[left]]:
                    have -= 1
                left += 1
        return s[res[0] : res[1] + 1] if resLen != float("infinity") else ""

    
        