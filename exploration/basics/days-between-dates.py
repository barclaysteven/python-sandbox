from datetime import date

f_date = date(2018, 8, 27)
l_date = date(2018, 9, 10)

delta = l_date - f_date
print(delta.days)
