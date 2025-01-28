# Offical solution
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


# Double pointer
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for e in s:
            if e.isalpha() or e.isdigit():
                filtered.append(e)
        new_str = "".join(filtered).lower()
        left, right = 0, len(new_str) - 1
        while right > left:
            if new_str[left] == new_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# check if string is the same forwards and backwards
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for e in s:
            if e.isalpha() or e.isdigit():
                filtered.append(e)
        new_str = "".join(filtered).lower()
        if new_str == new_str[::-1]:
            return True
        else:
            return False