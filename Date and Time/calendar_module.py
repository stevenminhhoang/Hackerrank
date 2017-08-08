from calendar import *
weekdays = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
date = list(map(int, input().split()))
i = weekday(date[2], date[0], date[1])
print(weekdays[i])
