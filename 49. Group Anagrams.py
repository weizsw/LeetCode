class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = {}

        for s in strs:
            key = tuple(sorted(s))
            ans[key] = ans.get(key, []) + [s]
        return ans.values()