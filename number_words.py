words = {1: "One",
         2: "Two",
         3: "Three",
         4: "Four",
         5: "Five",
         6: "Six",
         7: "Seven",
         8: "Eight",
         9: "Nine",
         10: "Ten",
         11: "Eleven",
         12: "Twelve",
         13: "Thirteen",
         14: "Fourteen",
         15: "Fifteen",
         16: "Sixteen",
         17: "Seventeen",
         18: "Eighteen",
         19: "Nineteen",
         20: "Twenty",
         30: "Thirty",
         40: "Forty",
         50: "Fifty",
         60: "Sixty",
         70: "Seventy",
         80: "Eighty",
         90: "Ninety",
         100: "Hundred",
         1000: "Thousand",
         1000000: "Million",
         1000000000: "Billion",
         1000000000000: "Trillion"}


units = (0, 1, 10, 100, 1000, 1000000, 1000000000, 1000000000000)


def get_word(num: int) -> str:
    res = words[num]
    if num in units[3:]:
        res = f"One {res}"
    return res


def num_to_words(num: int) -> str:
    if num == 0:
        return "Zero"
    if num in words:
        return get_word(num)

    res = []
    while num > 0:
        for idx, unit in enumerate(reversed(units[1:])):
            quotient, remainder = divmod(num, unit)
            if quotient*unit in words:
                res.append(get_word(quotient*unit))
                num = remainder
            elif quotient in words:
                res.append(f"{get_word(quotient)} {words[unit]}")
                num = remainder
            elif units[idx-1] < quotient < unit:
                res.append(f"{num_to_words(quotient)} {words[unit]}")
                num = remainder
            if remainder in words:
                res.append(get_word(remainder))
                return " ".join(res)
    return " ".join(res)


print(num_to_words(1))
print(num_to_words(10))
print(num_to_words(12))
print(num_to_words(110))
print(num_to_words(111))
print(num_to_words(211))
print(num_to_words(123))
print(num_to_words(1100))
print(num_to_words(1234))
print(num_to_words(100000))
print(num_to_words(12345))
print(num_to_words(123456))
print(num_to_words(1234567))
print(num_to_words(12345678))
print(num_to_words(123456789))
print(num_to_words(1234567891))