# coding: utf-8


class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split("/")
        stack = []
        for item in items:
            if item == "..":
                if stack:
                    stack.pop()
            elif item == "." or not item:
                pass
            else:
                stack.append(item)

        return "/" + "/".join(stack)


print(Solution().simplifyPath("/a/./b/../../c/"))
