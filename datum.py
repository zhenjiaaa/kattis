def datum():
    d, m = map(int, input().split())
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_in_months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # -1 is placeholder for indexing
    return day[(sum(days_in_months[1:m]) + d + 2) % 7]  # +2 is situational to the year and so is the leap year feb days


def datum2():
    import calendar
    d, m = map(int, input().split())
    return calendar.day_name[calendar.weekday(2009, m, d)]


print(datum())
