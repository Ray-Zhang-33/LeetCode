from typing import List

# Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        left, right = 1, 2
        for right in range(2, len(nums)):
            # check if right pointer is not equal to left pointer - 1
            if nums[right] != nums[left - 1]:
                left += 1
                nums[left] = nums[right]
        return left + 1

# Test cases
def test_removeDuplicates():
    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    expected_nums1 = [1, 1, 2, 2, 3]
    expected_length1 = 5

    # Test Case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected_nums2 = [0, 0, 1, 1, 2, 3, 3]
    expected_length2 = 7

    # Create an instance of the Solution class
    solution = Solution()

    # Test Case 1
    print("Test Case 1:")
    print("Input:", nums1)
    unique_length1 = solution.removeDuplicates(nums1)
    print("Output Length:", unique_length1)
    print("Modified Array:", nums1[:unique_length1])
    print("Expected Length:", expected_length1)
    print("Expected Array:", expected_nums1)
    assert unique_length1 == expected_length1 and nums1[:unique_length1] == expected_nums1, "Test Case 1 Failed"
    print("Test Case 1 Passed!\n")

    # Test Case 2
    print("Test Case 2:")
    print("Input:", nums2)
    unique_length2 = solution.removeDuplicates(nums2)
    print("Output Length:", unique_length2)
    print("Modified Array:", nums2[:unique_length2])
    print("Expected Length:", expected_length2)
    print("Expected Array:", expected_nums2)
    assert unique_length2 == expected_length2 and nums2[:unique_length2] == expected_nums2, "Test Case 2 Failed"
    print("Test Case 2 Passed!\n")

# Run the test cases
if __name__ == "__main__":
    test_removeDuplicates()