class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        for l, r, k, v in queries:
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % MOD
                i += k

        result = 0
        for j in nums:
            result ^= j
        
        return result