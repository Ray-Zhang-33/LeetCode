#include <vector>
#include <iostream>

class Solution2 {
    public:
    void rotate(std::vector<int>& nums, int k) {
        if (nums.size() == 0) {
            return;
        }
        int moves = k % nums.size();
        std::reverse(nums.begin(), nums.end());
        std::reverse(nums.begin(), nums.begin() + moves);
        std::reverse(nums.begin() + moves, nums.end());
        for (int i = 0; i < nums.size(); i++) {
            std::cout << nums[i] << " ";
        }
    };
};


// Basic solution, running out of time on super large input
class Solution1 {
public:
    void rotate(std::vector<int>& nums, int k) {
        if (nums.size() == 0) {
            return;
        }
        int moves = k % nums.size();
        for (int _ = 0; _ < moves; _++) {
            int end = nums.back();
            nums.pop_back();
            nums.insert(nums.begin(), end);
        }
    };
};


int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;

    Solution2 solution;

    std::cout << "Original array: ";
    for (int num : nums) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    std::cout << "Rotated array: ";
    solution.rotate(nums, k);

    return 0;
}