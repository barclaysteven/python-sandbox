from datetime import *

f_date = date(2019, 8, 27)
l_date = datetime.now().date()

delta = l_date - f_date
print(delta.days)
