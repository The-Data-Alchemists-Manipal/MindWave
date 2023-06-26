import requests
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
nltk.download('punkt')

def scrape_news_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    article_elements = soup.find_all('a', class_='post-block__title__link')

    articles = []
    for article in article_elements[:10]:  # Iterate through the first 10 articles
        title = article.text.strip()
        link = article['href']
        articles.append({'title': title, 'link': link})

    return articles

def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    summary = article.summary
    return summary

# Example usage
news_url = 'https://techcrunch.com/'
scraped_articles = scrape_news_articles(news_url)

for article in scraped_articles:
    title = article['title']
    link = article['link']

    print(f"Title: {title}")
    print(f"Link: {link}")

    summary = summarize_article(link)
    print("Summary:")
    print(summary)
    print()
