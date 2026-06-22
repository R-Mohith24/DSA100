class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i] , 0) + 1
            if hashmap[nums[i]] <= k:
                res.append(nums[i])

        return res
