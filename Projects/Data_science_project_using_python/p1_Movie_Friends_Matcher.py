# Movie Friends Matcher
#You have a list of users and the movies they like. Given a user's name, recommend another user who has the most movies in common.
users = [
    {"name": "Ali", "likes": ["Inception", "Interstellar", "The Matrix"]},
    {"name": "Sara", "likes": ["The Notebook", "Inception", "The Matrix"]},
    {"name": "John", "likes": ["Titanic", "Interstellar", "Avengers"]},
    {"name": "Ayesha", "likes": ["Inception", "Interstellar", "The Matrix", "Avengers"]},
    {"name": "Zara", "likes": ["The Matrix", "Inception"]}
]
# go through user list and store the liked movies
target_user = "Ali"
for user in users:
    if user['name'] == target_user:
        liked_movies = user['likes']
 # find the best match
max_match = 0
best_match = ""
# compare with other users
for user in users:
    if user['name'] != target_user:
        target_set = set(liked_movies)
        other_users_liked_movies = set(user['likes'])
        shared_movies = target_set.intersection(other_users_liked_movies)
        match_count = len(shared_movies)
        if match_count > max_match:
            max_match = match_count
            best_match = user['name']
            best_shared_movies = shared_movies
print("most similar user:", best_match, "with most shared movies:", max_match, "and shared movies are:", best_shared_movies)




