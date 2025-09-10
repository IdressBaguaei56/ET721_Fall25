"""
Joseph Bernabe
Lab 4, Dictionary Functions
Sep 10, 2025
"""
print("\n---------- Example 1: Dictionary ----------")
# Contact dictionary with three different users
contacts = {
    "Bill" : "718-111-2222",
    "Martha" : "646-000-3333",
    "Peter" : "212-000-1111"
}
print(contacts)

# Save a specific value of a key
user1 = contacts["Martha"]
print(f"User's phone number = {user1}")

# Add content to the dictionary
contacts["Anna"] = "646-222-3333"
print(contacts)

# Update value of a specific key
contacts["Peter"] = "800-000-0000"
print(contacts)

print("\n---------- Example 2: Loop through a dictionary ----------")
# Print each key in the dictionary
for i in contacts:
    print(i)

# Print each value in the dictionary
for i in contacts:
    print(contacts[i])

# Print each key:value set in the dictionary
for i in contacts:
    print(f"{i} = {contacts[i]}")

print("\n---------- Example 3: Length of a dictionary ----------")
print(f'Dictionary has {len(contacts)} users')

print("\n---------- Example 4: Copy a dictionary ----------")
copy_contacts1 = contacts.copy()
copy_contacts2 = dict(contacts)
print(copy_contacts1)
print(copy_contacts2)

print("\n---------- Example 5: Remove a key value pair in a dictionary  ----------")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("\n---------- Example 6: Add a key value pair in a dictionary  ----------")
contacts.update({"Lucas":"212-111-1111"})
print(contacts)

print("\n---------- Example 7: Returns items, key, and value pair in a dictionary  ----------")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Resturn values = {contacts.values()}")

print("\n---------- Example 8: Dictionary Applications ----------")
# Store in a dictionary the count of occurency of the word 
phrase = "to be or not to be"
list_phrase = phrase.split()
# create a empty dictionary 
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

# print result 
for word in word_count_dict:
    print(f"{word} = appears {word_count_dict[word]}")

print("\n------ EXCERCISE ------")
users = ["peterpan@yahoo.com","annie@hotmail.com","CArl@hotmail.com" ,"martha@gmail.com","cassie@yahoo.com","Josue@hotmail.com","John@hotmail.com"]
# Dictionary to keep track of counts
word_count_dict = {"gmail": 0, "hotmail": 0, "yahoo": 0}

# Loop through each email
for mail in users:
    mail = mail.lower()  # make lowercase so case doesn’t matter
    if "gmail" in mail:
        word_count_dict["gmail"] += 1
    elif "hotmail" in mail:
        word_count_dict["hotmail"] += 1
    elif "yahoo" in mail:
        word_count_dict["yahoo"] += 1

# Print results
for word in word_count_dict:
    print(f"{word} = appears {word_count_dict[word]}")
