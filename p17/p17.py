# how many characters in numbers from one to one thousand. Format is like 'one
# hundred and fortytwo'. Spaces don't count.

def Run():
    # All the worlds we care about.
    hund = "hundred"
    andw = "and"
    digits = ["one", "two", "three", "four", "five" "six",
              "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"]
    # Function for total number of characters in a bunch of strings
    f = lambda x: sum([len(el) for el in x])
    
    total = 90 * f(digits)
    # ones place. every number but the teens. so 9 per 100 times 10 hundreds
    
    total += 10 * f(teens)
    # weird special case for teens.
    
    total += 100 * f(tens)
    # the last two digits of everything.
    
    total += len(hund) * 900
    # hundreds - every number but 1 to 99 and one thousand.
    
    total += len(andw) * (900 - 9)
    # ands - every number but the x00s and 1 to 99

    total += 100 * f(digits)
    # for $x in $x hundred to $x hundred and ninety nine
    
    total += len("one") + len("thousand")
    # 1000
    print total


if __name__ == "__main__":
    Run()
