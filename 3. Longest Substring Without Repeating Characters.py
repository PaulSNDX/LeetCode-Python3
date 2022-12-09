# Linear time – O (n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = -1
        chars = {}
        ans = 0
        for i,ch in enumerate(s):
            if ch in chars and chars[ch] > j:
                j = chars[ch]
            else:
                if ans < i-j:
                    ans = i-j
            chars[ch] = i
        return ans

"""
# This implementation takes too much time
# Quadratic time – O (n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1: return length
        maxSubstringLength = 1
        for index, character in enumerate(s):
            uniqueCurrentSubstringChars = [character]
            tempLength = 1
            for item in range(index + 1, length):
                if s[item] in uniqueCurrentSubstringChars:
                    uniqueCurrentSubstringChars = [s[item]]
                    if tempLength > maxSubstringLength:
                        maxSubstringLength = tempLength
                    tempLength = 1
                    continue
                
                uniqueCurrentSubstringChars.append(s[item])
                tempLength += 1
            if tempLength > maxSubstringLength:
                maxSubstringLength = tempLength
        return maxSubstringLength
"""
