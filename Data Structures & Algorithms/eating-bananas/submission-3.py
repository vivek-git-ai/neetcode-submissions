class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = sum(piles)
        ans = high

        if len(piles) == 1:
            return math.ceil(piles[0]/h)

        def check_possible(h, rate, piles):
            count = 0
            for pile in piles:
                if rate >= pile:
                    count += 1
                else:
                    count += pile // rate

                    if pile % rate != 0:
                        count += 1

            if count <= h:
                return True
            else:
                return False    

        while low <= high:

            mid = (low + high) // 2

            if check_possible(h, mid, piles):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans                



            

            

            

        

        