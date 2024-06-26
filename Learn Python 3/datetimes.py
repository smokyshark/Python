from datetime import datetime
#Creating a date using a year, month and day as arguments, than time hour, minutes, seconds
birthday = datetime(1994, 2, 15, 4, 25, 12)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.weekday)
#creating a date using datetime.now()
now = datetime.now()
substraction = datetime(2018,1,1) - datetime(2017,1,1)
substraction2 = datetime.now() - datetime(2017,1,1)
print(substraction)
print(substraction2)

#Parsing a date using strptime
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date.month)


#Rendering a date as a string using strftime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y'
print (date_string)








































