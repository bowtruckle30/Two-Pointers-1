class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## T.C = O(n)
        ## S.C = O(1)
        
        low, mid = 0, 0
        high = len(nums) - 1
        
        while mid <= high:
            
            if nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            elif nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            else:
                mid += 1
        
