#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        auto findElement = std::find(nums.begin(), nums.end(), val);
        while (findElement != nums.end()) {
            nums.erase(findElement);
            findElement = std::find(nums.begin(), nums.end(), val);
        }
        int k = nums.size();
        return k;
    }
};

int main() {
    Solution solution;

    // test cases
    std::vector<int> nums = {3, 2, 2, 3};
    int val = 3;

    // call function and get result
    int k = solution.removeElement(nums, val);

    // output result
    std::cout << "k = " << k << std::endl;
    std::cout << "nums after removal: ";
    for (int i = 0; i < k; ++i) {
        std::cout << nums[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}