class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = float('-inf')  # Initialize maxSum as the lowest possible number
        currentSum = 0  # Tracks the running sum of the current subarray
        
        for num in nums:
            # If the current running sum is negative, discard it and start fresh
            if currentSum < 0:
                currentSum = 0

            # Add the current number to the running sum
            currentSum += num

            # Update maxSum if the current running sum is greater
            if currentSum > maxSum:
                maxSum = currentSum
                
        return maxSum


# ✅ Maximum Subarray - Kadane’s Algorithm (O(n) time, O(1) space)
#
# Walk through the array, and for each number:
# - If the current sum is negative, restart from current number (i.e. discard the previous subarray)
# - Otherwise, keep adding the number to the current subarray
# - Always track the max sum seen so far
#
# Example:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Step-by-step:
# - Start at -2 → currentSum = -2 → maxSum = -2
# - See 1 → currentSum = 1 → maxSum = 1
# - See -3 → currentSum = -2 (1 + -3) → maxSum = 1
# - See 4 → currentSum = 4 → maxSum = 4
# - See -1 → currentSum = 3 → maxSum = 4
# - See 2 → currentSum = 5 → maxSum = 5
# - See 1 → currentSum = 6 → maxSum = 6
# - See -5 → currentSum = 1 → maxSum = 6
# - See 4 → currentSum = 5 → maxSum = 6
# ✅ Answer: 6