class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}
        map2=[]
        for i in range(len(nums)):
            map1[nums[i]]=map1.get(nums[i],0)+1
        i=0
        sorted_items=sorted(map1.items(),key=lambda x:x[1],reverse=True)
        while i<k:
            map2.append(sorted_items[i][0])
            i=i+1
        return map2