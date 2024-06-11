class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        while len(common_prefix) < len(strs[0]):
            for i in range(len(strs)):
                if i == 0  and len(strs[i]) > len(common_prefix):
                    common_prefix += strs[i][len(common_prefix)]
                    continue

                if strs[i][:len(common_prefix)] != common_prefix:
                    return common_prefix[:-1]
            
        return common_prefix