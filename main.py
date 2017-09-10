#watcard_calculator.py
#This is a simple program which will determine, on average, how much of your meal plan you should spend daily in order to maximise it.

from datetime import datetime

#This function requests for the beginning date that the user would want to input.
def start_date():
    n = str(input("Residence Start Date (YYYY/MM/DD): "))
    try:
        dt_start = datetime.strptime(n, "%Y, %m, %d")
    except ValueError:
        print("Incorrect format")
    return dt_start

#This function requests for the end date that the user would want to input. 
def end_date():
    m = str(input("Residence End Date (YYYY/MM/DD): "))
    try:
        dt_end = datetime.strptime(m, "%Y, %m, %d")
    except ValueError:
        print("Incorrect format")
    return dt_end

#This function determines the number of days within the two dates.
def deltaD(start_date,end_date):
    deltaD = end_date - start_date
    return deltaD.days

#This function determines how many times in total the user will do laundry during the term.
def laundry(days):
    laundry = int(input("Number of times laundry is done in a week: "))
    weeks = days / 7
    return laundry*weeks

#This function calculates the average amount of money spent everyday using everthing calculated before.
def dailySpend(laundry, days):
    balance = float(input("Please enter your WatCard Balance: "))
    spend = (balance - (2*laundry))/days
    return spend

#The main function executes everything.
def main():
    start = start_date()
    end = end_date()
    days = deltaD(start, end)
    weeks = laundry(days)
    spend = dailySpend(weeks, days)
    print("You should spend ${:0.2f} every day.".format(spend))
    x = input("Enter any character to exit.")

main()
