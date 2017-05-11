# Program: DiesPerWafer
# Author:  Barret Fisher
# Section: 005
# Date:   9/10/12
# Purpose:
#   Program to find the area of a silicon wafer and calculate the number of chips (or dies) that will fit on its surface.
# Input:
#   User supplies diameter in mm (as a number, no error checking done) of silicon wafer and area of individual chips to be implanted in mm^2
#   (also as a number).
# Ouput:
#   User given surface area in mm^2 of wafer and number of chips that will fit on it.

from math import pi

def main():

# Greet the user
    print()
    print("            000 Slicing Wafers 000")
    print()

# Ask the user for the diameter of silicon wafer in mm
    waferWidth = eval(input("What is the diameter of the wafer to slice? (in mm) "))

# Ask the user for the area of a chip (or die) in mm^2
    chipArea = eval(input("What is the area of a single die? (in mm^2) "))

# ERROR CHECK, diameter AND chip area MUST be positive  
    if waferWidth > 0 and chipArea > 0 :
        
# Calculate the area of the wafer
        waferArea = pi * ( waferWidth / 2 ) * ( waferWidth / 2 )
        waferArea = round(waferArea, 2)

# Calculate the number of chips that will fit on the wafer
        diesPerWafer = waferWidth * pi * ( ( waferWidth / ( 4 * chipArea ) ) - ( 1 / ( 2 * chipArea )**0.5 ) )

# ERROR CHECK, is wafer big enough for die?
        if diesPerWafer > 0 :
            
# Output to shell the area of the wafer in mm^2
            print("From a wafer with area" ,waferArea, "square millimeters")

# Output to shell the whole number of chips that can fit on the wafer
            print("you can cut" ,int(diesPerWafer), "dies.")
            print("This does not take into account defective dies, alignment markings and test sites")
            print("on the wafer's surface.")

# ERROR CHECK, wafer is too small
        else:
            print("The wafer is too small to fit any die.")

# ERROR CHECK, diameter and chip area are not positive  
    else:
        print("The parameters for diameter or die area are invalid.")
        
main()
