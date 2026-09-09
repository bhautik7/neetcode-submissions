class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=float('-inf')
        seen=set()
        left=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxLen=max(maxLen,right-left+1)
        return maxLen if maxLen!=float('-inf') else 0