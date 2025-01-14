from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = []  # List to store unique elements
        for n in nums:
            if n not in unique_nums:
                unique_nums.append(n)  # Append unique elements
        nums[:] = unique_nums  # The slice assignment modifies the original list
        k = len(unique_nums)  # Length of unique elements
        return k

# Local debugging
if __name__ == "__main__":
    # Test case
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Input array
    expectedNums = [0, 1, 2, 3, 4]  # Expected result

    # Call the function
    solution = Solution()
    k = solution.removeDuplicates(nums)

    # Check the result
    print(f"Output: {k}, nums = {nums[:k]}")  # Print the result
    assert k == len(expectedNums)  # Check the length
    for i in range(k):  # Check the first k elements
        assert nums[i] == expectedNums[i]
    print("Test passed!")