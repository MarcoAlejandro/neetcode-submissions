class Solution:
    def __init__(self):
        self.DP = {}

    def numDecodings(self, s: str) -> int:
        self.DP[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            # If current char is 0, no decoding can start here
            if s[i] == "0":
                self.DP[i] = 0
                continue

            # Take one digit
            self.DP[i] = self.DP[i + 1]

            # Take two digits, only if valid
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                self.DP[i] += self.DP[i + 2]

        return self.DP[0]