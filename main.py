# Write a python program to convert kilometer to miles.


# Taking a user input
Kilometer = int(input("Enter the value of Kilometer: "))

#convversion factor
conv_factor = 0.621371

# calculate miles
Miles = Kilometer*conv_factor

print("%0.2f Kilometers is equal to %0.2f Miles " %(Kilometer, Miles))