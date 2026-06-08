class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        for i in range(len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
            else:
                return True
        return False


        