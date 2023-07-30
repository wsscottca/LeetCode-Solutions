class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        
        for string in strs:
            char_list = [0 for _ in range(26)]
            
            for char in string:
                index = ord(char) - ord('a')
                char_list[index] += 1
            
            char_tuple = tuple(char_list)
            if char_tuple in ana_dict:
                ana_dict[char_tuple].append(string)
                
            else:
                ana_dict[char_tuple] = [string]
                
        return ana_dict.values()