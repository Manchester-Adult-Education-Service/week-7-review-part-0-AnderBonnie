# -------------------------------------------
# Exercise 1: Review
# -------------------------------------------
# In this exercise, we’ll continue revising all the core Python concepts covered so far:
# - Variables, input(), and print()
# - Assignment and comparison operators
# - if, elif, and else conditionals
# - for and while loops
# - Lists
#
# Each task will be completed step-by-step by different learners.
# -------------------------------------------


# Task 1: Simple Profile
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Simple Profile\n"
    + "-------------------------------------------")
# Step 1:
# Ask the user for their name and favourite hobby.
# Store both in variables called `name` and `hobby`.
# Print a welcome message using both values.

# Example:
# Enter your name: Jordan
# Enter your favourite hobby: painting
# Output: Hello, Jordan! You enjoy painting.

# Write your code below:
name = input("What is your name?:")
hobby = input("What is your hobby?:").lower()
print (f"Hello, {name}! You enjoy {hobby}.")

# SWAP LEARNERS BEFORE THIS STEP
# Step 2:
# Now add another input asking for the user’s age (convert it to an integer using int()).
# Then print:
# “Jordan is 25 years old and enjoys painting.”
#
# Write your code below:
users_age = int(input("What is your age?:"))
print (f"{name} is {users_age} years old and enjoys {hobby}.")



# SWAP LEARNERS BEFORE THIS STEP
# Step 3:
# Add a condition:
# - If the user is under 40, print “You’re quite young to be into [hobby]!”
# - Otherwise, print “That’s a great hobby for oldies too!”
#
# Write your code below:
if users_age < 40:
    print (f"You' re quite young to be into {hobby}")
else :
    print ("That's a great hobby for oldies too!")



# Task 2: Counting
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Counting\n"
    + "-------------------------------------------")
# Step 1:
# Ask the user for a number between 1 and 10.
# Store it in a variable called `limit`.
# Use a for loop and range() to print all numbers from 1 up to that limit.

# Example:
# Enter a number: 5
# Output:
# Counting: 1
# Counting: 2
# Counting: 3
# Counting: 4
# Counting: 5

# Write your code below:
limit = int(input("Enter a number between 1 to 10:"))
for i in range (1, limit + 1):
    print (f"Counting: {i}")




# SWAP LEARNERS BEFORE THIS STEP
# Step 2:
# Now modify the loop to check if each number is even or odd.
# Print "x is even" or "x is odd" for each number.
#
# Write your code below:
for i in range(1, limit +1):
    if i % 2 == 0 :
        print(f"{i} is even.")
    else :
        print(f"{i} is odd.")


# Task 3: Shopping List Builder
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Shopping List Builder\n"
    + "-------------------------------------------")
# Step 1:
# Create an empty list called `shopping_list`.
# Ask the user to enter three items (one at a time).
# Append each item to the list.

# Example:
# Enter item 1: milk
# Enter item 2: eggs
# Enter item 3: bread
# Output list should be ['milk', 'eggs', 'bread']

# Write your code below:
shopping_list = []
item1 = input("Enter item 1:").lower().strip()
shopping_list.append (item1)
item2 = input("Enter item 2:").lower().strip()
shopping_list.append (item2)
item3 = input("Enter item 3:").lower().strip()
shopping_list.append (item3)
print("Your list so far:", shopping_list)


# SWAP LEARNERS BEFORE THIS STEP
# Step 2:
# Use a for loop to print each item in the list neatly, one per line.
# Example:
# Your shopping list:
# milk
# eggs
# bread
#
# Write your code below:
print("Your shopping list:")
for item in shopping_list:
    print(item)



# SWAP LEARNERS BEFORE THIS STEP
# Step 3:
# Ask the user for one more item to add.
# Append it to the list and print the updated list again.
#
# Write your code below:
new_item = input("Enter one more item:")
shopping_list.append(new_item)
print ("Updated shopping list:")
for item in shopping_list:
    print (item)


# Task 4: Number Guessing Game
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 4: Number Guessing Game\n"
    + "-------------------------------------------")
# Step 1:
# Create a variable called `secret_number` and set it to any number between 1 and 10.
# Ask the user to guess the number.
#
# Write your code below:
secret_number = 5
guess = int(input("Guess the secret number between 1 and 10:"))

# SWAP LEARNERS BEFORE THIS STEP
# Step 2:
# Add an if/else structure:
# - If the guess matches the secret number, print “Correct!”
# - Otherwise, print “Wrong, try again!”
#
# Write your code below:
if guess == secret_number:
    print ("Correct!")
else:
    print ("Wrong, try again!")    



# SWAP LEARNERS BEFORE THIS STEP
# Step 3:
# Use a while loop to keep asking until the user guesses correctly.
# Print “Well done!” when they finally get it right.
#
# Write your code below:

while guess != secret_number:
    guess = int(input("Wrong, try again:"))
print ("Well done! You guessed it!")    




# Task 5: Average Calculator
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 5: Average Calculator\n"
    + "-------------------------------------------")
# Step 1:
# Ask the user how many numbers they want to enter.
# Store this number in a variable and convert it to an integer.

# Write your code below:
count = int(input("How many numbers would you want to enter?"))

# SWAP LEARNERS BEFORE THIS STEP
# Step 2:
# Create an empty list called `numbers`.
# Use a for loop to ask the user for that many numbers.
# Convert each input to int() and append it to the list.
#
# Write your code below:
numbers = []
for i in range (count):
    num = int(input(f"Enter number {i + 1}:"))
    numbers.append(num)


# SWAP LEARNERS BEFORE THIS STEP
# Step 3:
# Calculate the average (sum of all numbers / how many numbers there are)
# Print the result using an f-string like:
# "The average of your numbers is X"
#
# Write your code below:
average = sum(numbers) / len(numbers)
print(f"The average of your number is {average}.")

# -------------------------------------------
# EXTENSION ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension: Student Score Feedback\n"
    + "-------------------------------------------")
# Step 1:
# Ask the user to enter three test scores (as integers).
# Calculate the average score.

# SWAP LEARNERS BEFORE THIS STEP
# Step 2:
# Use if/elif/else to give feedback:
# - 70 or more → “Excellent!”
# - 50–69 → “Good effort!”
# - Below 50 → “Needs improvement.”
#
# Then print the student’s average and their feedback message.
#
# Example:
# Enter scores: 70, 65, 80 → Output: Average = 71.6, Excellent!
#
# Write your code below:




# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
