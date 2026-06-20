class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = float('inf')

        while low <= high:
            if nums[low] < nums[high]:
                ans = min(ans,nums[low])
                break

            mid = (low + high) // 2
            ans = min(nums[mid], ans)

            if nums[mid] >= nums[low]:
                #left side is sorted
                low = mid + 1
            else:
                high = mid - 1 

        return ans        









        