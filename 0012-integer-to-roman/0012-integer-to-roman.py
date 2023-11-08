'''
Timestamps:
    Understand and Cases: 1:52
    Design and Verify: 14:01
    Code:
    
Understand and Cases:
    num = 3999
    num = 49
    num = 772
    
Design and Verify:
    Go 1000s > 100s > 10s > 1s
    Add together the result
    
    dict?
    list of strings e.g. M = ["", "M", "MM", "MMM"]
    index
    for thousands num // 1000
    3000 -> 3 -> M[3] = "MMM"
    
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    hundreds (num % 1000) // 100
    900 -> 9 -> C[9] = "CM"
    
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    tens (num % 100) // 10
    90 -> 9 -> X[9] = "XC"
    
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ones (num % 10)
    9 -> I[9] = "IX"
    
    Combine
    return (thousands + hundreds + tens + ones)
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        thousands = M[num // 1000]
        hundreds = C[(num % 1000) // 100]
        tens = X[(num % 100) // 10]
        ones = I[num % 10]
        
        return (thousands + hundreds + tens + ones)