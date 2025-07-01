# project 3 related to data science
# Favorite Color Count
# Given a list of people and their favorite colors, count how many people like each color. Then suggest the most popular color to new users.
#                 sample Data
people = [
    {"name": "Ali", "favorite_color": "blue"},
    {"name": "Sara", "favorite_color": "green"},
    {"name": "John", "favorite_color": "blue"},
    {"name": "Ayesha", "favorite_color": "red"},
    {"name": "Zara", "favorite_color": "green"},
    {"name": "Bilal", "favorite_color": "blue"},
    {"name": "Noor", "favorite_color": "yellow"},
    {"name": "Usman", "favorite_color": "green"},
    {"name": "Fatima", "favorite_color": "red"},
]
def people_most_liked_color(people):
    color_appears = {}
    for person in people:
        color = person["favorite_color"]
        if color  in color_appears:
            color_appears[color] += 1
        else:
            color_appears[color] = 1
    print(color_appears)
      # most popular color that user liked
    most_liked_color = max(color_appears, key=color_appears.get)
    return most_liked_color
popular_color = people_most_liked_color(people)
print("suggestion the most popular color to new users is:", popular_color)