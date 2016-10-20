"""
"Statistic Calculator"

Program asks user to enter list of integers. Make statistic calculations,
based on entered data set. Offers user to continue or finish work, after computing.
"""

import re
import time

# Asks user for input and converts it to int.
def converting():
	# Asking for input and converting it to list of strs. (using regular expressions)
	str_numbers = re.findall('[+-]?\d+', raw_input("\nEnter list of numbers, separated by commas: "))
	numbers = []
	# Converting list of str --> list of int
	for i in str_numbers:
		i = int(i)
		numbers.append(i)

	print "\nData Set:\n", numbers
	return numbers

# Finding median
def median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) / 2
    if len(numbers) % 2 == 0:
        return sum(numbers[middle - 1:middle + 1]) / 2
    else:
        return numbers[middle]

# Finding upper and lower Quartiles
def quartiles(numbers):
	numbers = sorted(numbers)
	middle = len(numbers) / 2
	lowerQ = median(numbers[:middle])
	upperQ = median(numbers[middle:])
	return lowerQ, upperQ

# Finding Minimum and Maximum Value
def min_max(numbers):
	return min(numbers), max(numbers)

# Finding Average
def average(numbers):
	return sum(numbers) / len(numbers)

# Finding Outliers
def outliers(numbers):
	Q1, Q3 = quartiles(numbers)
	outlier = []
	outlier.append(Q1 - 1.5 * (Q3 - Q1))
	outlier.append(Q3 + 1.5 * (Q3 - Q1))
	return outlier

#Main function
def main():

	numbers = converting()
	
	print "\n\nMinimum value = %d \n\nMaximum value = %d" % min_max(numbers)
	print "\nAverage value = ", average(numbers)
	print "\nMedian = ", median(numbers)
	print "\nLower Quartile = %d \n\nUpper Quartile = %d" % quartiles(numbers)
	print "\nOutliers = ", outliers(numbers)
	
	# Asks user if he wish to continue or exit calculator, and takes input from user.
	answer = raw_input("\n\n\t\t\tDo you want to make new calculations, Y/N? ")
	# Conditional statement, that checks user decision
	if answer == "y" or answer == "Y":
		main()
	elif answer == "n" or answer == "N":
		print "\n\t\t\tThank you for using 'Statistic Calculator'\n\t\t\tThe program will now exit"
		time.sleep(3)
	else:
		print "\n\t\t\tWrong input, the program will now exit!"
		time.sleep(3)

print "\n\t\t\tWelcome to Statistic Calculator!"

main()

