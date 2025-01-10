#include <iostream>  // For input and output
#include <vector>    // For std::vector
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int left = 0;
        for (int right = 0; right < n; right++) {
            if (nums[right] != val) {
                nums[left] = nums[right];
                left++;
            }
        }
        return left;
    }
};

// Main function for testing
int main() {
    Solution solution;

    // Test case
    vector<int> nums = {3, 2, 2, 3}; // Input array
    int val = 3;                     // Value to remove

    // Call the removeElement function
    int k = solution.removeElement(nums, val);

    // Output the results
    cout << "Number of elements after removal: " << k << endl;
    cout << "Modified array: ";
    for (int i = 0; i < k; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}