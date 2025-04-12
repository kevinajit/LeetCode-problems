class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        nums.sort(reverse = True)
        
        if len(nums) > 2:
            return nums[2]

        else:
            return nums[0]
        
# ✅ Third Maximum Number - Clean O(n log n) solution using set and sort
#
# Step 1: Convert the list to a set to remove duplicates.
# Step 2: Sort the unique elements in descending order.
# Step 3: 
#   - If there are 3 or more distinct elements, return the third one.
#   - Otherwise, return the largest (first) element.
#
# Example 1:
# Input: [3, 2, 1] → Unique sorted: [3, 2, 1] → Return 1 (third max)
#
# Example 2:
# Input: [1, 2] → Unique sorted: [2, 1] → Not enough elements → Return 2 (max)
#
# Example 3:
# Input: [2, 2, 3, 1] → Unique sorted: [3, 2, 1] → Return 1 (third max)