class Solution:
    def romanToInt(self, s: str) -> int:
        # dictionary for easily calculating value
        conversion_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        sum = 0
        index = 0
        
        while index < len(s):
            curr = conversion_dict[s[index]]
            next = None
            
            if (index + 1) < len(s):
                next = conversion_dict[s[index+1]]
                
            if next and next > curr:
                curr = next - curr
                index += 1
            
            sum += curr
            index += 1
        
        return sum
                
                