
def Run():
    # jan 31
    # feb 28
    # march 31
    # apr 30
    # may 31
    # jun 30
    # jul 31
    # aug 31
    # sep 30
    # oct 31
    # nov 30
    # dec 31
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday']
    # start year 1900
    year = 1900
    total = 0
    # start on a monday
    day = 1

    while year < 2001:
        for i, num in enumerate(months):
            day += num
            # leap year
            if (i == 1 and year % 4 == 0 and 
               (year % 100 != 0 or year % 400 == 0)):
                day += 1
            day = day % 7
            if day == 0 and year > 1900 and not (year == 2000 and i == 11):
                total += 1
        year += 1
    print total

if __name__=="__main__":
    Run()
