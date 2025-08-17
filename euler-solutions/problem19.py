from enum import Enum


class Month(Enum):
	January = 0
	February = 1
	March = 2
	April = 3
	May = 4
	June = 5
	July = 6
	August = 7
	September = 8
	October = 9
	November = 10
	December = 11


def days_in_month(month: Month, year: int):
	match month:
		case Month.January:
			return 31
		case Month.February:
			return 28 + int(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
		case Month.March:
			return 31
		case Month.April:
			return 30
		case Month.May:
			return 31
		case Month.June:
			return 30
		case Month.July:
			return 31
		case Month.August:
			return 31
		case Month.September:
			return 30
		case Month.October:
			return 31
		case Month.November:
			return 30
		case Month.December:
			return 31


class DayOfWeek(Enum):
	Monday = 0
	Tuesday = 1
	Wednesday = 2
	Thursday = 3
	Friday = 4
	Saturday = 5
	Sunday = 6


def next(day: DayOfWeek, num_days: int):
	return DayOfWeek((day.value + num_days) % 7)


year = 1901
day = DayOfWeek.Tuesday
month = Month.January
sundays = 0
while year < 2001:
	prev_month = month
	if day == DayOfWeek.Sunday:
		sundays += 1
	if month == Month.December:
		year += 1
		month = Month.January
	else:
		month = Month(month.value + 1)
	day = next(day, days_in_month(prev_month, year))
	# print("{day} {month} {year}".format(month=month.name, day=day.name, year=year))
print(sundays)
