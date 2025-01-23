from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        appear_times = (len(nums) + 1) // 2
        for n in set(nums): # it excceds time limit if using for n in nums
            if nums.count(n) >= appear_times:
                return n

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3, 2, 3]
    print(solution.majorityElement(nums1))  # expected output: 3
    
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(solution.majorityElement(nums2))  # expected output: 2