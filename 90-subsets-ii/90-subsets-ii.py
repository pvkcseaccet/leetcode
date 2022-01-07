class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output, self.len = [], len(nums)
        nums.sort()
        def _helper(idx, current_set_length, current_set):
            if current_set_length == len(current_set):
                self.output.append(current_set[:])
                return
            for j in range(idx, self.len):
                if (j != idx and nums[j] == nums[j-1]): continue
                current_set.append(nums[j])
                _helper(j + 1, current_set_length, current_set)
                current_set.pop()
        
        for i in range(self.len + 1):
            _helper(0, i, [])
        return self.output