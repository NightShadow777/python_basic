data = float(input("Ввод: "))
data = int(data)
data, seconds = divmod(data, 60)
data, minutes = divmod(data, 60)
days, hours = divmod(data, 24)

if days % 10 == 1 and days % 100 != 11:
    days_str = " день, "
elif days % 10 > 1 and days % 10 < 5:
    days_str = " дня, "
else:
    days_str = " дней, "

result = "{0}{1}{2}:{3}:{4}".format(str(days), days_str, str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2))
print(result)
