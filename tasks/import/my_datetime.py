from datetime import datetime, timedelta
#Вывод текущей даты и времени
now_time = datetime.now()
print(f"Текущаяя дата и время --- {now_time}")
#Разница между датами
dayX = datetime(year=2025,month=11,day=16)
next_bithday = (dayX - now_time).days

if next_bithday < 0:
    # Если день рождения уже прошёл, добавляем год
    birthday = dayX.replace(year=now_time.year + 1)
    days_until_birthday = (birthday - now_time).days
    
print(f"До следующего дня рождения осталось -- {next_bithday} дней")