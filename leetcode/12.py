# coding: utf-8

class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        res = ""
        for key in hash_map:
            t = num // key
            if t > 0:
                res += hash_map[key] * t
            num = num % key

        return res


print(Solution().intToRoman(1994))
