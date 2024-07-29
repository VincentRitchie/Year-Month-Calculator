#-----------------------------------------------------THE FOLLOWING CALCULATES THE MONTHS AND YEAR-----------------------------------------------------
# YEAR AND MONTHS CALCULATION
# Leap year calculation function
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Bellow is the month-day calculation function
def month_days(year, month):
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # List of days in each month
    if leap_year(year) and month == 2: # Leap year February has 29 days
        return 29 # Leap year February has 29 days
    else:
        return days_list[month - 1] # Subtracting 1 to get the previous month's days
    
# Bellow is the main function to calculate the days in a given month and year
year = int(input("Enter the year: "))
month = int(input("Enter the month: ")) 
days = month_days(year, month)  # Passing year and month to Calculate days in the given month and year
print(f"The number of days in month {month} of year {year} is {days}.")