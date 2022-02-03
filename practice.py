from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
em_id=input("Enter Your Employee_ID_No: ")
print(dt_string,em_id)	

 

from datetime import datetime
my_string1 = str(input('Enter date you want to book meeting(yyyy-mm-dd)'))
my_string2= str(input('Enter time you want to book meeting(hh:mm)'))
my_date = datetime.strptime(my_string1, "%Y-%m-%d")
my_time = datetime.strptime(my_string2, "%I:%M %p")
Hours=int(input("enter how many hours meeting slot you want:"))
result= my_date,my_time,Hours
print(my_date,my_time,Hours)




















# timestamp = time.strftime('%H:%M:%S')


# from datetime import *
# m2 = '1:35 PM'
# m2 = datetime.strptime(m2, '%I:%M %p')
# print(m2)
# # 1900-01-01 13:35:00


# from datetime import datetime
# m2 = '1:35 PM'
# in_time = datetime.strptime(m2, "%I:%M %p")
# out_time = datetime.strftime(in_time, "%H:%M")
# print(out_time)
# 13:35


# from datetime import datetime
# d = datetime.strptime("23:56", "%H:%M")
# print(d.strftime("%I:%M"))
# d.strftime("%I:%M" %p)
# '6:56 PM'
