import basics;
import datetime

benji = basics.Doggo('Benji', 2, True)
benji.bark()

x = datetime.datetime(2021, 4, 20)
print(x)

now = datetime.datetime.now()
print(now.year)
print(now.strftime("%D"))


