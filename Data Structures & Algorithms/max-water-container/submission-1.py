class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        ans = 0

        while low < high:

            minimum = min(heights[low],heights[high])

            current_ans = minimum * abs(high-low)

            if current_ans > ans:
                ans = current_ans

            if heights[low] < heights[high] :
                low += 1
            else:
                high -= 1

        return ans                

            

            

        






        