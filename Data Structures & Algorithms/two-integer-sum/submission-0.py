class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i in range(len(nums)):
            check = target - nums[i]

            if check not in bucket:
                bucket[nums[i]] = i
            else:
                return[bucket[check],i]    



            


            

        