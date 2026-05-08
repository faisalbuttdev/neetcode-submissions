class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        count=[[]for i in range(len(nums)+1)]
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for num,freq in hashmap.items():
            count[freq].append(num)
        res=[]
        for i in range(len(count)-1,0,-1):
                for num in count[i]:
                 res.append(num)
                 if k==len(res):
                  return res
            
        
