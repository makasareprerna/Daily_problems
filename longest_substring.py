'''

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''

list = []
def lengthOfLongestSubstring(s):
        charset = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l +=1
            charset.add(s[i])
            res = max(res, i-l+1)
        return res






s = "abcabcbb"
lengthOfLongestSubstring(s)

