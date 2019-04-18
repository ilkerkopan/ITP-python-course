# week 11 hackernews api usage sample
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
top_stories_request = requests.get(url)
top_stories = top_stories_request.json()

for i in range(5):
    url = "https://hacker-news.firebaseio.com/v0/item/"+str(top_stories[i])+".json"
    r = requests.get(url)
    item = r.json()
    print(f'title:{item["title"]} url:{item["url"]}')
    