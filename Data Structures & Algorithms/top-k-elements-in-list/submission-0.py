class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for numbers in nums:
            if numbers in dic:
                dic[numbers] += 1
            else:
                dic[numbers] = 1

        buckets = [[] for _ in range(len(nums)+ 1 )]
        
        for n , freq in dic.items():
            buckets[freq].append(n)
        
        result =[]

        for freq in range(len(buckets)-1,0,-1):
            for n in buckets[freq]:
                result.append(n)
            

            if len(result) == k:
                return result
    
    