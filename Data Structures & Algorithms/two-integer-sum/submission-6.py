class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            print(hashmap)
            if diff  in hashmap:
                print(diff,nums[i],target)
                return [hashmap[diff],i]
            hashmap[nums[i]]=i
        return []