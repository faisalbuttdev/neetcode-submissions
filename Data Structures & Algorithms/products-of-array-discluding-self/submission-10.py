class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        prefix=[1]*size
        suffix=[1]*size
        res=[0]*size
        for i in range(1,size):
            prefix[i]=nums[i-1]*prefix[i-1]
        for i in range(size-2,-1,-1):
            suffix[i]=nums[i+1]*suffix[i+1]

        for i in range(size):
            res[i]=prefix[i]*suffix[i]
        print("P: ",prefix,"\nS: ",suffix)
        return res