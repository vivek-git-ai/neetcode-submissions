class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums.sort()

        bucket = {}

        ans = []

        for num in nums:
            if num not in bucket:
                bucket[num] = 1
            else: 
                bucket[num] = bucket[num] + 1

        count_list = []
        
        for num, count in bucket.items():
            count_list.append((count, num))

        count_list.sort(reverse=True)


        for i in range(k):
            ans.append(count_list[i][1])

        return ans    

        

            










     



                


        