# coding: utf-8

class Solution:
    def confusingNumber(self, n: int) -> bool:
        num_map = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6" 
        }
        str_n = str(n)
        new_str_n = ""

        for s in str_n:
            r_s = num_map.get(s)
            if r_s is None:
                return False
            new_str_n = r_s + new_str_n

        return str_n != new_str_n
            
print(Solution().confusingNumber(916))
print(Solution().confusingNumber(69))
print(Solution().confusingNumber(68))
