'''
Timestamps:
     Cases:
     Verify:
     Code:
     
Cases:
    cpdomains = ["100000000 coachable.dev"]
    cpdomains = ["10 coachable.dev", "10 poachable.dev"]

Design:
    dict
    
    for cpdomain in cpdomains:
        split = cpdomain.indexOf(" ")
        count = int(cpdomain[:split])
        
        subdomain = cpdomain[split:]
        subdomains = [subdomain]
        
        while subdomain.indexOf(".") != -1:
            sd_split = subdomain.indexOf(".")
            subdomain = subdomain[sd_split:]
            subdoamins.append(subdomain)
        
        for subdomain in subdomains:
            if subdomain in dict:
                dict[subdomain] += count
            else:
                dict[subdomain] = count
    
    res = []
    for subdomain, visits in dict:
        as_string = str(visits) + subdomain
        res.append(as_string)
        
    return res
'''

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts_dict = {}
    
        for cpdomain in cpdomains:
            split = cpdomain.index(" ")
            count = int(cpdomain[:split])

            subdomain = cpdomain[split+1:]
            subdomains = [subdomain]

            while subdomain.find(".") != -1:
                sd_split = subdomain.index(".")
                subdomain = subdomain[sd_split+1:]
                subdomains.append(subdomain)

            for subdomain in subdomains:
                if subdomain in counts_dict:
                    counts_dict[subdomain] += count
                else:
                    counts_dict[subdomain] = count

        res = []
        for subdomain in counts_dict.keys():
            visits = counts_dict[subdomain]
            as_string = str(visits) + " " + subdomain
            res.append(as_string)

        return res