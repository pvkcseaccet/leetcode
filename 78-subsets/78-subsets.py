class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.sets = []
        def _helper(idx, curSetLength, current):
            if curSetLength == len(current):
                self.sets.append(current[:])
                return
            
            for j in range(idx, len(nums)):
                current.append(nums[j])
                _helper(j + 1, curSetLength, current)
                current.pop()
        
        for i in range(len(nums) + 1):
            _helper(0, i, [])
        return self.sets