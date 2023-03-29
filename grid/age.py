import datetime
s = input("------>")
birthday = datetime.date(int(s[0:4]),int(s[5:7]),int(s[8:]))
Now = datetime.datetime.today().date()
print(birthday)
print(Now)
age = Now - birthday
delta = datetime.date(1,1,1) + (age)
delta1 = delta - datetime.date(1,1,1)
datevalue = datetime.date.isoformat(delta1)
print(delta)
print(datevalue)