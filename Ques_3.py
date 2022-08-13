# Write the python program to display the calender ?
import calendar

# taking the user input in the form of YYYY and MM

YY =int(input("Enter the year: "))
MM = int(input("Enter the MM: "))

print(calendar.month(YY,MM))