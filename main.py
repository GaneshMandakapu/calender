import calendar
y= int(input("Which Year you wanna see"))
m = 1
print("__CALENDER__")

Cal = calendar.TextCalendar(calendar.SUNDAY)

i=1
while i<=12:
    Cal.prmonth(y,i)
    i+= 1