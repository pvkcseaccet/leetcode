class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        canSortNumsInDescending = num < 0
        if canSortNumsInDescending: num = -1 * num
        nums = map(str, sorted(list(str(num))))
        if canSortNumsInDescending:
            nums = list(reversed(nums))
        zeroes = ""
        for i in nums:
            if int(i) == 0:
                zeroes += str(i)
        getString = lambda lists: "".join(i for i in lists)
        return '-' + getString(nums) if canSortNumsInDescending else getString(nums[len(zeroes)]) + zeroes + getString(nums[len(zeroes)+1:])