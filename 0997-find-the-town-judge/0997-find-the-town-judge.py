'''
Timestamps:
    Cases: 1:20
    Design: 3:37
    Verify: 4:45
    Code: 11:19
    
Understand and Cases:
    No edge cases

Design and Verify:

    3
    3: 2
    2: 0
    1: 1

    O(n)
    add all to dictionary with counts of trust
    go through the dictionary for each one that everyone trusts
    find the one that trusts no one
    if they all trust someone return -1
'''


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        
        # until populated no one trusts anyone
        def default_value():
            return 0
        
        # dict for trust count and set for everyone that trusts someone
        trust_dict = defaultdict(default_value)
        trustees = set()
        
        # populate our data structures
        for trustee, trusted in trust:
            trust_dict[trusted] += 1
            
            if trustee not in trustees:
                trustees.add(trustee)
        
        # for each member, check if everyone trusts them (n-1 in trust dict)
        # and they don't trust anyone (not in trustee set)
        # whoever meets these conditions is the judge
        for member in trust_dict.keys():
            if trust_dict[member] == n - 1 and member not in trustees:
                return member
            
        # if no one meets the conditions return -1
        return -1