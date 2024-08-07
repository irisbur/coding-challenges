class Solution:
    def __init__(self):
        self.units = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }
        self.teens = {
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 
            18: "Eighteen", 19: "Nineteen"
        }
        self.tens = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        result = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                result = self.hundredsToWords(num % 1000) + " " + self.thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()

    def hundredsToWords(self, num: int) -> str:
        result = ""
        if num >= 100:
            result += self.units[num // 100] + " Hundred"
            num %= 100
        if num >= 20:
            result += " " + self.tens[num // 10]
            num %= 10
        if 0 < num < 10:
            result += " " + self.units[num]
        elif 10 <= num < 20:
            result += " " + self.teens[num]
        return result.strip()

# Example usage
sol = Solution()
print(sol.numberToWords(1234567))  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"