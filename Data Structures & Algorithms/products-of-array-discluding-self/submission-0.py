class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        def product_array(nums):
            product = 1
            for num in nums:
                product = product * num

            return product

        for i in range(len(nums)):
            
            array = nums[:i] + nums[i+1:] 
            result.append(product_array(array))

        return result   

                


        