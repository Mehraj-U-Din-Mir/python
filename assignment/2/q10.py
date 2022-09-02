"""Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)"""


from datetime import datetime
curr_dt=datetime.now()
print(" The current date and time is")

print (curr_dt.strftime("%d-%m-%y %H:%M:%S"))
