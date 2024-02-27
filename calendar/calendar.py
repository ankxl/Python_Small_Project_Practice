"""
Calendar Maker by Ankit Rai
The program takes as input a valid year (AD only) and valid month (1 to 12)
and produces a calendar for the month. The calendar is saved to a text file.
"""

import datetime

DAYS = ["Sunday",'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
MONTHS = ['January','February','March','April','May','June','July','August',
          'September','October','November','December']

def get_calendar_yr_mon(year, month):
    # The text field will contain the details of the calendar. 
    text = ""

    # Header for the month and year
    text = text + " "*40 + f"{MONTHS[month-1]} {year}\n"
    
    # Header for days of the week
    text += "....Sunday...." + "....Monday...." + "....Tuesday..." + "...Wednesday.." + "...Thursday..." + "....Friday...." + "...Saturday....\n"
    
    # Header border for new rows
    rows = "+-------------" *7 +"+\n"

    # Blank rows to be inserted after date row
    blank = "|             "*7 + "|\n"

    cur_date = datetime.date(year,month,1)

    # Loop moves back the date to the last sunday on or before 1st of the month    
    while True:
        day = cur_date.weekday()
        # Check if current date is Sunday (weekday == 6)
        if day != 6:
            # if day is not Sunday move back 1 day
            cur_date -= datetime.timedelta(days=1)
        else:
            # first sunday found and break out of the loop
            break
    
    # The loop runs through the first week to the last week
    # exit criteria checks if the month is no longer current month
    while True:
        # Prints the calendar header row with +- just above the date row
        text += rows

        # Run the loop seven times (for seven days) to print the row
        for _ in range(7):
            date = cur_date.day
            # add one day column to text
            text += f"| {date:>2}          "
            # roll forward the date by 1 day
            cur_date += datetime.timedelta(days=1)
        # Close the line for row
        text += "|\n"

        # Add blank lines
        text += blank *3

        # Exit criteria: Month changed to next month 
        if month != cur_date.month:
            break
    
    # Calendar last weeks footer
    text += rows
    return text


def main():
    print('Calendar Maker by Ankit R')

    year = 0
    month = 0
    while True:
        if year == 0:
            print("Enter the year for the calendar:")
            response = input("> ")

            if response.isdecimal() and int(response) > 0:
                year = int(response)
            else:
                print("Please enter a valid year i.e. numeric and greater than 0")
        if year != 0 and month == 0:
            print("Enter the month for the calendar, 1 - 12:")
            response = input("> ")

            if response.isdecimal() and (0 < int(response) <= 12):
                month = int(response)
                break
            else:
                print("Please enter a valid month i.e. numeric and greater than 0 and less than and equal t0 12")
                print("i.e. 3 for March, 6 for June")
            
    text = get_calendar_yr_mon(year,month)
    print(text)

    # Write the calendar to the file with name "Calendar_MONTH_Year.txt"
    filename = f"Calendar_{MONTHS[month-1]}_{year}.txt"

    with open(filename,"w") as f:
        f.write(text)
    
    print(f"Calendar pasted on the file - {filename}")

if __name__ == '__main__':
    main()