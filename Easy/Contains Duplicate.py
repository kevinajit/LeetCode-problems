class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique elements we've seen so far
        seen = set()

        for num in nums:
            if num in seen:
                return True  # Duplicate found
            else:
                seen.add(num)

        return False


# ✅ Contains Duplicate - O(n) time, O(n) space using a set
#
# Iterate through the list while storing each number in a set.
# If a number is already in the set, we’ve found a duplicate and return True.
# Otherwise, keep adding unseen numbers to the set.
#
# Example:
# nums = [1, 2, 3, 1]
# Step 1: seen = {1}
# Step 2: seen = {1, 2}
# Step 3: seen = {1, 2, 3}
# Step 4: see 1 again → already in set → return True