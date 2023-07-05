# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# для простоты договоримся, что год может быть в диапазоне [1, 9999].
# весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале 
# с передачей даты на проверку.

from sys import argv

MAX_YEAR = 9999
MIN_YEAR = 1
MAX_MONTH = 12
MIN_MONTH = 1
MONTH_31 = [1, 3, 5, 7, 8, 10, 12]
MONTH_30 = [4, 6, 9, 11]
DAY_31 = 31
DAY_30 = 30
MIN_DAY = 1
LAEP_FEB = 29
FEB = 28

def check_data(data : str) -> bool:
    day, month, year = map(int, data.split('.'))

    if not MIN_YEAR <= year <= MAX_YEAR:
        return False
    if not MIN_MONTH <= month <= MAX_MONTH:
        return False
    if month in MONTH_31 and not MIN_DAY <= day <= DAY_31:
        return False
    if month in MONTH_30 and not MIN_DAY <= day <= DAY_30:
        return False
    if month == 2 and _check_year(year) and not MIN_DAY <= day <= LAEP_FEB:
        return False
    if month == 2 and not _check_year(year) and not MIN_DAY <= day <= FEB:
        return False
    return True

def _check_year(y : str) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

if __name__ == '__main__':
    print(check_data(argv[1]))