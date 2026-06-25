class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        Pcount , Scount = {} , {}
        for i in range(len(p)):
            Pcount[p[i]] = Pcount.get(p[i] , 0) + 1
            Scount[s[i]] = Scount.get(s[i] , 0) + 1

        res = [0] if (Pcount) == (Scount) else []

        left = 0
        for right in range(len(p) , len(s)):
            Scount[s[right]] = Scount.get(s[right] , 0) + 1
            Scount[s[left]] -= 1

            if Scount[s[left]] == 0:
                Scount.pop(s[left])
            left += 1
            if (Scount) == (Pcount):
                res.append(left)

        return res