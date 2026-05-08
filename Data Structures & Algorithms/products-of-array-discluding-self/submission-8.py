class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        for i in range(len(nums)):
            mul=1
            for k in range(len(nums)):
                if k!=i: 
                 mul*=nums[k]
            product.append(mul)

        return product