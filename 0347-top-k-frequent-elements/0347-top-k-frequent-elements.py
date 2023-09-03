import heapq

'''
Timestamps:
    Understand and cases: 4:00
    Design and Verify: 13:38
    Code: 27:38
    
Preparation:
    Understand and cases:
        nums = [] k = 0
        nums = [1] k = 0
        nums = [2,2,2,4,4,4,5,5,5] k = 2
        nums = [1,1,1,2,2,3,3,3,3] k = 2 
    Design and Verify:
        dictionary to store the ints and their frequencies
        min heap of tuples with the frequency as the first element
        
        for each number
            check if its in the dictionary
                if it is add 1 to its value
                if not add it with the frequency of 1
                
        for each key in the dictionary
            create a tuple of our frequency and key
            check if the min heap has k elements
                if it does, check if the frequency of the lowest item is lower than our current frequency
                    if it is pop it and push our current tuple
                    if not just continue
                if it does not
                    add our current tuple to the min heap
                    
        result list
        for tuple in min_heap:
            grab the value and add to our result list
        
        return our result list
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        min_heap = []
        
        # Populate our frequency dict
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            
            else:
                freq_dict[num] = 1
                
        # Get k largest frequency by using min_heap
        for key in freq_dict.keys():
            # Create our tuple with the frequency as the first element for our min_heap to function
            tup = (freq_dict[key], key)
            
            # Check if our min_heap is full
            if not min_heap or len(min_heap) < k:
                # If it isn't just add the current tuple
                heapq.heappush(min_heap, tup)
            
            else:
                # if it is check if the frequency is higher than the lowest in the min_heap
                if tup[0] > min_heap[0][0]:
                    # if it is then remove it and add our current tuple
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, tup)
        
        # Get just the values since we dont need the frequencies
        res = []        
        for tup in min_heap:
            res.append(tup[1])
        
        return res
                