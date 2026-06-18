class Solution: # find t in s as shortest
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        countT, countS = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have, need = 0, len(countT)
        res, res_len = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            char = s[right]
            countS[char] = 1 + countS.get(char, 0)

            if char in countT and countS[char] == countT[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                countS[s[left]] -= 1

                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1
        
        left, right = res
        return s[left: right + 1] if res_len != float('infinity') else ''