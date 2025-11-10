# Write to code in pyhton to check whether a given year is leap year or not.
'''
What is a Leap Year?
A leap year is a year that has an extra day added to it, making it 366 days long instead of the usual 365 days. This extra day is added to the month of February, which has 29 days in a leap year instead of the usual 28 days. Leap years are introduced to keep our calendar year synchronized with the astronomical year or seasonal year.
In Real Life:
1. Calendar Adjustment: Leap years help to correct the discrepancy between the calendar year and the solar year, ensuring that seasons occur at the same time each year.
2. Birthdays: People born on February 29th, known as "leaplings" or "leapers," celebrate their birthdays only in leap years.
3. Financial Calculations: In finance, interest calculations may take leap years into account for more accurate computations.
4. Event Planning: Events that are scheduled on a specific date may need to consider leap years for accurate planning.
5. Software Development: Programmers need to account for leap years when developing date and time-related applications to avoid errors.
'''
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# Example usage:
if __name__ == "__main__":
    year = 2020
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

    year = int(input("Enter a year to check if it is a leap year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
# The function works by checking the divisibility rules for leap years: a year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.
# Edge cases such as century years are handled by the additional check for divisibility by 400
year = int(input("Enter a year to check if it is a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")