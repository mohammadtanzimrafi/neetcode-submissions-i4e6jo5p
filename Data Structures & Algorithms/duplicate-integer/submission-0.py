class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        temp_set =  {i for i in nums}
        if len(nums) != len(temp_set):
            flag = True

        return flag