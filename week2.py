import os
import datetime
d = datetime.date.today()
d1 = datetime.timedelta(weeks=2)

res = d + d1
i = 0
while i != 10:
    print(res)
    res += d1
    i += 1


file_name = 't'
print(os.path.exists(file_name))

