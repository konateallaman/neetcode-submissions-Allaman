class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def helper():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                helper()

                # Undo
                path.pop()
                used[i] = False

        helper()

        return result