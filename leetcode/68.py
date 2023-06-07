# coding: utf-8
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        count = 0
        for word in words:

            if count + len(word) + len(line) > maxWidth:
                res.append(line)
                line = []
                count = 0

            line.append(word)
            count += len(word)

        if not res or res[-1] != line:
            res.append(line)

        str_res = []
        for line in res[:-1]:
            n = len(line)
            blank_count = maxWidth - sum(len(word) for word in line)
            while blank_count > 0:
                for i in range(n-1 if n != 1 else 1):
                    line[i] += " "
                    blank_count -= 1
                    if blank_count <= 0:
                        break

            str_res.append("".join(line))

        last_line_str = " ".join(res[-1])
        last_line_str += " " * (maxWidth - len(last_line_str))
        str_res.append(last_line_str)

        return str_res


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(Solution().fullJustify(words, maxWidth))
