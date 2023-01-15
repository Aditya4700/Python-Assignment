import datetime

#for days
today_date = datetime.date.today() # Today's Date
date_obj = datetime.date(2022, 5, 21) # 21st May, 2021 - A Date Object

print(date_obj - today_date) # Output Days with Time
print((date_obj - today_date).days) # Will only output number of days

#for time
curr_time = datetime.datetime.now().time() # Current Time
# print(curr_time) # Around 00:10:00
dt_obj = datetime.time(8,10,20)
# print(dt_obj)
# Now Calculate the difference
diff = datetime.timedelta(hours=(dt_obj.hour - curr_time.hour), minutes=(dt_obj.minute - curr_time.minute), seconds=(dt_obj.second - curr_time.second))
print(diff)