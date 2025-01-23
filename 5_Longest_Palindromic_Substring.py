class Solution1:
    def longestPalindrome(self, s: str) -> str:
        # if s has 1 or 0 character, return s
        n = len(s)
        if n < 2:
            return s
        
        # ready for dp
        max_len = 1
        left = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(n):
            dp[i][i] = True

        # start enumeration
        for L in range(2, n + 1): # L is the length of substring
            for i in range(n): # i is the start index of substring
                j = i + L - 1 # j is the end index of substring
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                # update result
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    left = i
        return s[left:left + max_len]


# time: 4752ms
# find same letter from head and tail, then check if it is the same in reverse
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        gap = 1
        res = s[0]
        for i in range(len(s)): # start from left 
            if len(s[i:]) < gap:
                # Optimization: End traversal when the remaining length is less than gap (no longer possible to find a longer palindrome)
                break
            for j in range(-1, -len(s), -1): # start from right
                if len(s[i:len(s)+j+1]) <= gap or i == len(s) + j + 1:
                    # Optimization: End traversal when the remaining length is less than gap (no longer possible to find a longer palindrome)
                    break
                if s[i] == s[j]:
                    seq, reverse_seq = s[i:len(s)+j+1], s[i:len(s)+j+1][::-1]
                    if seq == reverse_seq and len(seq) > gap:
                        res, gap = seq, len(seq)                 
        return res


def test_solution(solution_class):
    print(f"Testing {solution_class.__name__}:")
    
    s1 = "babad"
    expected1 = "bab"
    result1 = solution_class().longestPalindrome(s1)
    print(f"Input: {s1}, Expected: {expected1}, Result: {result1}")
    
    s2 = "cbbd"
    expected2 = "bb"
    result2 = solution_class().longestPalindrome(s2)
    print(f"Input: {s2}, Expected: {expected2}, Result: {result2}")
    
    print()

test_solution(Solution1)
test_solution(Solution2)