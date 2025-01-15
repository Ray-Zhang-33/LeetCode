#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        int n = nums.size();
        std::unordered_set<int> unique_elements;
        int left = 0;
        for (int right = 0; right < n; right++) {
            if (unique_elements.find(nums[right]) == unique_elements.end()) {
                unique_elements.insert(nums[right]);
                nums[left] = nums[right];
                left++;
            }
        }
        return left;
    }
};

// Helper function to print the array
void printArray(const std::vector<int>& nums, int k) {
    for (int i = 0; i < k; i++) {
        std::cout << nums[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Test case 1
    std::vector<int> nums1 = {1, 1, 2};
    Solution solution;
    int k1 = solution.removeDuplicates(nums1);
    std::cout << "Test case 1: " << k1 << ", nums = ";
    printArray(nums1, k1); // Expected output: 2, nums = 1 2

    // Test case 2
    std::vector<int> nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int k2 = solution.removeDuplicates(nums2);
    std::cout << "Test case 2: " << k2 << ", nums = ";
    printArray(nums2, k2); // Expected output: 5, nums = 0 1 2 3 4

    return 0;
}