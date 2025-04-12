class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n²)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # O(n)
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[num], index]
            else:
                num_to_index[num] = index

# ✅ Two Sum - Optimized O(n) solution using dictionary
#
# For each number in the list, calculate its "complement" (target - num).
# If the complement has already been seen and stored in the hash map, 
# we’ve found the two indices that add up to the target.
# Otherwise, store the current number and its index in the hash map.
#
# Example:
# nums = [2, 7, 11, 15], target = 9
# Step 1: store 2 → {2: 0}
# Step 2: see 7, check if 2 exists → yes → return [0, 1]