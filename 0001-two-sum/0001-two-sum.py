class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement already exists
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store current number with index
            num_map[num] = i