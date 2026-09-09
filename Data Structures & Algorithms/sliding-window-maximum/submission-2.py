import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heap=[]
        # result=[]
        # for i in range(len(nums)):
        #     heapq.heappush(heap,(-nums[i],i))
        #     if i >= k-1:
        #         while heap[0][1] <= i-k:
        #             heapq.heappop(heap)
        #         result.append(-heap[0][0])
        # return result
        n=len(nums)
        dq=deque()
        result=[]

        for i in range(n):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)

            if dq[0] <= i-k:
                dq.popleft()
            
            if i >= k-1:
                result.append(nums[dq[0]])
        return result