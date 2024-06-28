import requests
from bs4 import BeautifulSoup

def fetch_news(keywords):
    url = f'https://news.google.com/rss/search?q={keywords}&hl=zh-CN&gl=CN&ceid=CN:zh-Hans'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    news_list = []
    for item in items:
        news = {
            'title': item.title.text,
            'link': item.link.text,
            'pubDate': item.pubDate.text
        }
        news_list.append(news)
    return news_list

def main():
    keywords = '关系词'
    news = fetch_news(keywords)
    for n in news:
        print(f"Title: {n['title']}\nLink: {n['link']}\nDate: {n['pubDate']}\n")

if __name__ == "__main__":
    main()
