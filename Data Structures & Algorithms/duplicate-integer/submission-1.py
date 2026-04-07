class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        if len(set(nums)) != len(nums):
            flag = True

        return flag