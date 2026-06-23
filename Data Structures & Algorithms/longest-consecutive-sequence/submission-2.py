class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket = set(nums)
        longest_streak = 0
        

        for num in bucket:
            if num - 1 not in bucket:
                current_num = num
                current_streak = 1

                while current_num + 1 in bucket:
                    current_streak += 1
                    current_num += 1


                longest_streak = max(longest_streak,current_streak)

        return longest_streak    







       


        