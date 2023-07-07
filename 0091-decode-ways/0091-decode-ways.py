#2611055971756562
#                010
#               110
#              111
#             111
#            111
#           111
#          111
#         211
#        221
#       222
#      222
#     222
#    022
#   202
#  220
# 222
#422


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)
        
        dp_last = 1
        dp_two_prev = 0
        curr = 0
        
        for i in reversed(range(n)):
            curr = 0
            print(s[i])
            if s[i] != "0":
                curr = dp_last
            
            if (i + 1 < n) and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):
                curr += dp_two_prev
                
            print(f'curr: {curr}, last: {dp_last}, two_prev: {dp_two_prev}')

            dp_two_prev = dp_last
            dp_last = curr
            
                
        return curr