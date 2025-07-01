# project 2 related to data science
#Book recomnended by ta
          # Data for the project
books = [
    {"title": "The Silent Patient", "tags": ["mystery", "thriller"]},
    {"title": "Pride and Prejudice", "tags": ["romance", "classic"]},
    {"title": "The Da Vinci Code", "tags": ["mystery", "fiction"]},
    {"title": "To Kill a Mockingbird", "tags": ["fiction", "classic"]},
    {"title": "Gone Girl", "tags": ["mystery", "fiction", "thriller"]},
    {"title": "The Fault in Our Stars", "tags": ["romance", "fiction"]}
]

user = {
    "name": "Sara",
    "liked_tags": ["fiction", "mystery"],
    "read_books": ["The Da Vinci Code"]
}
def recommended_books_by_tags(user, books):
    recommended_books = []
    user_tag = set(user['liked_tags'])
# loop through all books
    for book in books:
        if book['title'] not in user['read_books']:
            books_tag_set = set(book['tags'])
            similar_tag = books_tag_set.intersection(user_tag)
            if similar_tag:
                recommended_books.append({
                    "title": book['title'],
                    "tags": book['tags'],
                    "similar_tag_count": len(similar_tag)
                    })
    sorted_recommendations = sorted(recommended_books, key= lambda x:x['similar_tag_count'], reverse = True )
    return sorted_recommendations
result = recommended_books_by_tags(user, books)
print("recommended books for:", user['name'], result)