import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Function to scrape news articles
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

# Function to summarize an article
def summarize_article(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Identify the HTML element that contains the article content
    article_content = soup.find('div', class_='article-content')

    # Extract the article text
    paragraphs = article_content.find_all('p')
    article_text = ' '.join([p.get_text() for p in paragraphs])

    # Use Hugging Face's transformers pipeline for summarization
    summarizer = pipeline("summarization")
    summary = summarizer(article_text, max_length=150, min_length=30, do_sample=False)

    return summary[0]['summary_text']

# Example usage
news_url = 'https://techcrunch.com/'
scraped_articles = scrape_news_articles(news_url)

for article in scraped_articles:
    title = article['title']
    link = article['link']

    print(f"Title: {title}")
    print(f"Link: {link}")

    summary = summarize_article(link)
    print("Summary:", summary)

    print()
