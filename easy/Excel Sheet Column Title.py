class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            digit = (columnNumber - 1) % 26
            title = chr(ord("A") + digit) + title
            columnNumber = (columnNumber - 1) // 26

        return title
