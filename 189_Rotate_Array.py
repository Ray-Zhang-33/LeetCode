class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        moves = k % len(nums)
        nums[:] = nums[-moves:] + nums[:-moves]


solution = Solution()
nums = [1, 2]
k = 3
solution.rotate(nums, k)
print(nums)