# Task 1: You have a list of names where some are lowercase, some uppercase, etc. Clean the list to title case.
names = ["john", "SARA", "mOhIt"]
cleaned_name= []
for name in names:
    cleaned_name.append(name.title())
print(cleaned_name)

#Task 2: Clean a list of user comments by removing extra spaces and fixing alignment.
comments = ["  hello world  ", "  nice  work", "good  job "]
cleaned_comment = []
for comment in comments:
    result = " ".join(comment.strip().split())
    cleaned_comment.append(result)
print(cleaned_comment)

# Task 3: Given a list of emails, filter out those that don’t contain "@" or don’t end in .com.
emails = ["john@example.com", "noatsign.com", "hello@world", "filter@123.edu"]
cleaned_emails = []
# Output: ['john@example.com']
for email in emails:
    if "@" in email and email.endswith((".com", ".org", ".edu")):
        cleaned_emails.append(email)
print(cleaned_emails)

#Task 4: Given a list of user entries (name, email, age), count how many fields are missing.
users = [
    ["Ali", "ali@example.com", "22"],
    ["Sara", "", "19"],
    ["", "", ""]
]
# Output: Total missing fields = 4
counter = 0
for user in users:
    for value in user:
        if value == "":
            counter +=1
print("Total missing fields =", counter)

#Task 5: From a list of string ages like ["12", "18", "twenty", "25"], convert valid ones and return those ≥ 18.
ages = ["12", "18", "twenty", "25"]
# Output: [18, 25]
new_ages = []
for age in ages:
    try:
        num = int(age)
        if num >= 18:
            print(num)
            new_ages.append(num)
    except ValueError:
        pass
print(new_ages)

#Task 6: Given a list of phone numbers, keep only those that: Contain exactly 11 digits, Start with "03" (like a Pakistani number)
phones = ["03123456789", "123456", "03999887766", "04123456789", "0300123456"]
# Output: ['03123456789', '03999887766']
cleaned_phones = []
for phone in phones:
    if len(phone) == 11 and phone.startswith("03") and phone.isdigit():
        cleaned_phones.append(phone)
print(cleaned_phones)

# Task 7: Given a list of full names as lowercase strings, title-case each part separately.
names = ["john doe", "sara khan", "mOhIt ali"]
# Output: ['John Doe', 'Sara Khan', 'Mohit Ali']
new_names = []
for name in names:
    title_words = []
    for words in name.split():
       title_words.append(words.title())
    full_name = " ".join(title_words)
    new_names.append(full_name)
print(new_names)

# task 8: Task: From a list of valid emails, extract just the part before "@".
emails = ["john@example.com", "sara@gmail.com", "invalid.com"]
# Output: ['john', 'sara']
new_emails = []
for email in emails:
    if "@" in email:
        result = email.split("@")
        new_emails.append(result[0])
print(new_emails)


# Task 9: Task: From a list of emails, return unique ones only, treating "Ali@Gmail.com" and "ali@gmail.com" as duplicates.
emails = ["ali@gmail.com", "Ali@Gmail.com", "sara@yahoo.com"]
# Output: ['ali@gmail.com', 'sara@yahoo.com']
unique_emails = []
for email in emails:
    if email.lower() not in unique_emails:
        unique_emails.append(email)
        
print(unique_emails)


# Task 10: In user records, replace any missing value ("") with "N/A".
users = [
    ["Ali", "ali@example.com", "22"],
    ["Sara", "", "19"],
    ["", "", ""]
]
# Output: [['Ali', 'ali@example.com', '22'], ['Sara', 'N/A', '19'], ['N/A', 'N/A', 'N/A']]
new_users = []
for user in users:
    cleaned_user = []
    for value in user:
        if value == "":
            cleaned_user.append("N/A")
        else:
            cleaned_user.append(value)
            
    new_users.append(cleaned_user)
print(new_users)