# Zargham-abbas
# zarghamabbas859@gmail.com

# Question_7:
# Write a program that takes user input for their age and prints a message addressing their age group (e.g., "Teenager," "Adult"). Explore user interaction and conditional statements in Python.

# Ask the user to input their age:
age = int(input("Enter your age :"));

# Determine the age group based on the input:
if age >= 0 and age <= 12:
    print("Your age group is child");
elif age >= 13 and age <= 19:
    print("Your age group is teenager");
elif age >= 20 and age <= 59:
    print("Your age group is Adult");
else :
    print("You are a senior citizen");

# Run!
# DONE!