'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''
# Initialize an empty list to store the two-digit numbers
list_digits = list()

# Iterate through each line of the document
file = open ('2023/Day1/lines.txt').read().splitlines()
for line in (file):
    digits = [char for char in line if char.isdigit()]
    concatenated_digits = digits[0] + digits[-1]    # Concatenate the first and last digit of the line
    list_digits.append(concatenated_digits)    # Append to the list_lines

# Convert the list of strings to a list of integers
# This is necessary for summing the values later
list_integers = [int(i) for i in list_digits]

# Sum all the two-digit numbers together
calibration_values = sum(list_integers)
print(calibration_values)