class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary={}
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]]=nums[i]
                print(dictionary)
            else:
                return True
        return False