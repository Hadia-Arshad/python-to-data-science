# json module
# problem 1 Create a Python dictionary of your profile (e.g. name, age, skills), then convert it to a JSON string using json.dumps().
import json
python_data = {"name": "Hadia", "age": 22, "skills": ["Python", "Data Science"]}
json_string = json.dumps(python_data)
print(json_string)
print(type(json_string))
print("THE END")
# problem 2 Take the dictionary from Problem 1 and save it into a file named profile.json using json.dump().
with open("profile.json", "w") as file:
    json.dump(python_data, file)
print("THE END")
#problem 3 Read the profile.json file created earlier and print the name and skills using Python.
with open("profile.json", "r") as file:
    json.load(file)
print(python_data["name"])
print(python_data["skills"])
print("THE END")
#problem 4 Given the following JSON string: json_data = '{"course": "Python", "duration": 45, "topics": ["Variables", "Loops", "Functions"]}' Convert it to a Python dictionary and print each key-value pair in a new line.
json_data = '{"course": "Python", "duration": 45, "topics": ["Variables", "Loops", "Functions"]}'
convert_in_python = json.loads(json_data)
for key, values in convert_in_python.items():
    print(f"{key}: {values}")
print("THE END")
# problem 5 Add a new key-value pair "city": "Lahore" to your existing profile.json file and save the updated version.
with open("profile.json", "r") as file:
    profile_data = json.load(file)
profile_data["city"] = "Lahore"
with open("profile.json", "w") as file:
    json.dump(profile_data, file, indent=4)
print("updated profile with city added:")
print(profile_data)
print("THE END")
# problem 6 Create a list of 3 dictionaries, each representing a user with name, age, and skills. Save the list into a file called profiles.json.
students = [{"name": "Hadia", "age": 22, "skills": ["python", "data science"]},
            {"name": "rohan", "age": 23, "skills": "java"},
            {"name": "Ali", "age": 21, "skills": "html"}]
with open("profile.json", "w") as file:
    json.dump(students, file, indent=4)
print("saved students profile in profile.json")
print("THE END")
# problem 7 Read profiles.json and print the names of users who have "Python" in their skills.
with open("profile.json", "r") as file:
    profile_data = json.load(file)
for user in profile_data:
    if any(skill.lower() == "python" for skill in user["skills"]):
        print(user["name"])
print("THE END")
# problem 8 Convert this nested JSON string to a Python dictionary and print the student's city:
nested_json = '{"student": {"name": "Ali", "details": {"age": 23, "city": "Karachi"}}}'
python_dictionary = json.loads(nested_json)
print(python_dictionary["student"]["details"]["city"])
print("THE END")
# problem 9 Read profile.json and count how many keys it has (e.g., name, age, skills, etc.), and print the total.
with open("profile.json", "r") as file:
    data = json.load(file)
count_keys = len(data[0].keys())
print(count_keys)
print("THE END")
#problem 10 Read profile.json and print it in a pretty format with indentation and sorted keys.
with open("profile.json", "r") as file:
    data = json.load(file)
pretty_output = json.dumps(data, indent= 4, sort_keys = True)
print(pretty_output)
print("THE END")