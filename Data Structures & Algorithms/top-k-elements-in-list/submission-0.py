from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums) #get each number and their frequency
        my_buckets=[[] for _ in range(len(nums)+1)] # create a bucket
        for num, frequency in count.items():
            my_buckets[frequency].append(num)
        result=[]
        for frequency in range(len(my_buckets) -1, 0, -1):
            for num in my_buckets[frequency]:
                result.append(num)
                if len(result)==k:
                    return result
        return result
            