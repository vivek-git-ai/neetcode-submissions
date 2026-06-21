class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low , high = 0,1
        ans = 0

        while high < len(prices):

            profit = prices[high] - prices[low]

            if profit < 0:
                low = high
                high +=1

            else:
                ans = max(ans,profit)
                high += 1  


        return ans          


    
            


            



        