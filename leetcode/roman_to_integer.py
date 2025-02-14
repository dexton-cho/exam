class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sr={"I": 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
        dr={"IV" : 4,"IX" : 9,"XL" : 40,"XC" : 90,"CD" : 400,"CM" : 900}
        x=0
        for i in range(len(s)):
            if s[i:i+2] in dr:
                x = x + dr[s[i:i+2]] - sr[s[i+1]]
            else:
                x += sr[s[i]]
        return x