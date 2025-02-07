"""
- Dictionary:
    -- We have option to store multiple values like list of names, list of ids etc
    -- Here we can keep DUPLICATE values
    -- Here, MANUALLY we can/need to provide index to each value called KEY/VALUE pair
"""

print("Dictionary PART-1")
print("Store Values")
print("-"*20)
# ---------------

my_dictionary_1 = {0:10, 1:"python", 2:"online"}

# FOR KEYS: We can make use of IMMUTABLE values like numbers, strings, tuple
my_dictionary_2 = {"duration":10, "course":"python", "mode":"online"}

# FOR VALUES: We can store any type of values in dictionary
my_dictionary_3 = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)

print("#"*40, end="\n\n")
###########################

print("Dictionary PART-2")
print("Access values using KEY")
print("-"*20)
# ---------------

my_dictionary = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n") # 10

print("Course:", my_dictionary["course"]) # "python"
print("2nd char in Course:", my_dictionary["course"][1], end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("Get the last option of Mode:", my_dictionary["mode"][-1]) # "offline"
print("3rd char of last option in Mode:", my_dictionary["mode"][-1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("LName of the Trainer:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd char in LName of the Trainer:", my_dictionary["trainer"]["lname"][1]) # "y"

print("#"*40, end="\n\n")
###########################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ---------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# GET course name
print("Course Name:", my_dictionary["course"])
print("Course Name using get() method:", my_dictionary.get("course"), end="\n\n")

# ADD/UPDATE
my_dictionary["location"] = "India"
# If key present then UPDATE else add new entry
print("my_dictionary after updating/adding 'location':", my_dictionary)

new_dictionary = {"trainer": "abc"}
my_dictionary.update(new_dictionary)
# If key present then UPDATE else add new entry
print("my_dictionary after updating/adding 'trainer':", my_dictionary)

# Delete
my_dictionary.pop("duration")
print("my_dictionary after removing 'duration':", my_dictionary)
my_dictionary.popitem()
print("my_dictionary after removing last value:", my_dictionary)

print("#"*40, end="\n\n")
###########################