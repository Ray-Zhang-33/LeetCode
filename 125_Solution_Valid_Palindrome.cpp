#include <vector>
#include <iostream>
#include <string>

class Solution {
public:
    bool isPalindrome(std::string s) {
        std::string sgood;
        for (char ch: s) {
            if (isalnum(ch)) {
                sgood += tolower(ch);
            }
        }
        std::string sgood_rev(sgood.rbegin(), sgood.rend());
        return sgood == sgood_rev;
    }
};

int main() {
    Solution solution;
    std::string s;
    s = "abcba";
    if (solution.isPalindrome(s)) {
        std::cout << s << " is a palindrome." << std::endl;
    } else {
        std::cout << s << " is not a palindrome." << std::endl;
    }
    
    return 0;
}