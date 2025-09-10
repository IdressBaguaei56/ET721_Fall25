"""
Idress Baguaei 
Lab3 , Python conditional statement and loops 
Sep 8, 2025
"""
# conditional statement 
print("\n ----- Example 1: if, elif, else, (EXCERCISE) -----")
"""
Modify Example 1:
- use while loop to validate if the user_number is between 1 and 9 
- user can only guess three times. This can be done using a for loop or a while 
"""
correct_num = 7
attempts = 0

while attempts < 3:
    ex_num = int(input(f"Enter a number between 1 and 9: "))

    if ex_num <= 1 or ex_num >= 9:
        print(f"Error {ex_num} is not valid. Please enter a number between 1 and 9.")
        continue  

    if ex_num == correct_num:
        print("Yay you did it")
        break
    else:
        print(f"Error {ex_num} is not the right number.")
        attempts += 1
else:
    print("Sorry, you ran out of tries.")

# Guess number between 1 and 9 
GUESS_NUM = 8
# Collect the number 
user_number = int(input("Guess a number: "))
# Compare 
if (user_number == GUESS_NUM):
    print(f"Great Job! {user_number} is the Guess Number")
elif(user_number>GUESS_NUM):
    print(f" {user_number} should be lower")
elif(user_number<GUESS_NUM):
    print(f"{user_number} should be higher")
else:
    print(f"ERROR!")

print("End of guessing!")

print("\n ----- Example 2: control flow loops with logical operators  -----")
# 'and', 'or' 'not' operators.
# 'and', operatore returns TRUE only aif all statments are true 
# 'or', operator returns TRUE if at least ONE of the statement is true
# 'not', operator returns the invert the logic. True --> not operator --> false 
"""
Example 2: 
- children under the age of 9 are only given milk for breakfast 
- children from 10 to 14 are given a sandwich 
- children from 15 to 17 are given a burger 
"""
age_student = int(input("Enter a age: "))
lunch = "None"
if age_student <9 and age_student>=5:
    lunch = "milk"
elif age_student >=10 and age_student<=14:
    lunch = "sandwich"
elif age_student>=15 and age_student<=17:
    lunch = "burger"
else:
    lunch = "None"

print(f" At age {age_student} the food is {lunch}")

print("\n ----- Example 3: for loops -----")
#'for' loop enables the program to execute a code block multiple times.
for n in range(3,10):
    print(n)

print("\n ----- Example 4: for loop in a list -----")
years =[2011, 2005, 19, 1998, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")

print("\n ----- Example 5: while loop as a counter  -----")
count = 1 
while count <=5:
    print(count)
    count += 1 

print("\n ----- Example 6: while loop to validate a number  -----")
# validate if a number is between -5 and 5 (inclusive)
num = int(input("Enter a number between -5 and 5: "))
# use a while to recollect if the num is invalid 
while num <-5 or num>5:
    num = int(input("ERROR! Enter a number between -5 and 5: "))

print(f"Enter a number = {num}")
