uni_to_word = {
    0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}
teens_map = {
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}
tens_map = {
    2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty",
    7: "Seventy", 8: "Eighty", 9: "Ninety"
}
thun_map = {
    0: "", 1: "Thousand", 2: "Million", 3: "Billion"
}


class Solution:
    def numberToWords(self, num: int) -> str:
        word = ""
        i = 0
        if num == 0:
            return "Zero"
        while num > 0:
            last_three_d_to_word = hun_to_words(num % 1000)
            if i > 0 and last_three_d_to_word != '':
                space = " " if word != '' else ''
                word = last_three_d_to_word + " " + thun_map[i] + space + word
            else:
                if word != '':
                    word = last_three_d_to_word + word
                else:
                    word = last_three_d_to_word
            i += 1
            num //= 1000
        return word


def hun_to_words(num):
    word = ""
    uni_d = num % 10
    ten_d = num // 10 % 10
    hun_d = num // 100
    if uni_d == 0 and ten_d == 0 and hun_d == 0:
        return ""
    if hun_d != 0:
        word += uni_to_word[hun_d] + " Hundred"
    if ten_d == 1:
        space = "" if word == "" else " "
        word += space + teens_map[ten_d * 10 + uni_d]
    elif ten_d != 0 and ten_d != 1:
        space = "" if word == "" else " "
        uni_d = " " + uni_to_word[uni_d] if uni_d != 0 else ""
        word += space + tens_map[ten_d] + uni_d
    elif ten_d == 0 and uni_d != 0:
        space = "" if word == "" else " "
        word += space + uni_to_word[uni_d]
    return word
