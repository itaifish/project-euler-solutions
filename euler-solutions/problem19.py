from enum import Enum
from time import perf_counter


# class Month(Enum):
# 	January = 0
# 	February = 1
# 	March = 2
# 	April = 3
# 	May = 4
# 	June = 5
# 	July = 6
# 	August = 7
# 	September = 8
# 	October = 9
# 	November = 10
# 	December = 11

# class DayOfWeek(Enum):
# 	Monday = 0
# 	Tuesday = 1
# 	Wednesday = 2
# 	Thursday = 3
# 	Friday = 4
# 	Saturday = 5
# 	Sunday = 6


def weekday_offset(month: int, year: int):
	match month:
		case 0:
			return 3
		case 1:
			return int(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
		case 2:
			return 3
		case 3:
			return 2
		case 4:
			return 3
		case 5:
			return 2
		case 6:
			return 3
		case 7:
			return 3
		case 8:
			return 2
		case 9:
			return 3
		case 10:
			return 2
		case 11:
			return 3


def next(day: int, num_days: int):
	new_day = day + num_days
	if new_day >= 7:
		new_day -= 7
	return new_day


def solve():
	year = 1901
	day = 1
	month = 0
	sundays = 0
	while year < 2001:
		prev_month = month
		if day == 6:
			sundays += 1
		if month == 11:
			year += 1
			month = 0
		else:
			month = month + 1
		day = next(day, weekday_offset(prev_month, year))
	return sundays


start = perf_counter()
result = solve()
end = perf_counter()
print(result)
print(end - start)
