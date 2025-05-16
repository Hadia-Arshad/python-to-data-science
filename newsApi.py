import requests
api_key = 'ae9e0f0befd44a75bcb0ac66f40cdd3d'
query = input("what type of news are you intrsted in")
url = f'https://newsapi.org/v2/everything?q={query}&apikey={api_key}'
response = requests.get(url)
news = response.json()
for i, article in enumerate(news['articles'][:5],start=1):
    print(f"{i}.{article['title']}")
