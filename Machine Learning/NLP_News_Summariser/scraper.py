import requests
from bs4 import BeautifulSoup

def scrape_news_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Identify the HTML elements that contain the article information
    article_elements = soup.find_all('a', class_='post-block__title__link')

    articles = []
    for article in article_elements:
        # Extract the relevant information from the article elements
        title = article.text.strip()
        link = article['href']

        # Create a dictionary with the extracted information
        article_data = {
            'title': title,
            'link': link
        }

        articles.append(article_data)

    return articles

# Example usage
news_url = 'https://techcrunch.com/'
scraped_articles = scrape_news_articles(news_url)

for article in scraped_articles:
    title = article['title']
    link = article['link']

    # Process the article information as per your requirements
    print(f"Title: {title}")
    print(f"Link: {link}")
    print()
