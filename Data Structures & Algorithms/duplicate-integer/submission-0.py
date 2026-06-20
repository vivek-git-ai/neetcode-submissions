class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        bucket = {}

        for num in nums:
            if num not in bucket:
                bucket[num] = 1

            else:
                return True

        return False            

        