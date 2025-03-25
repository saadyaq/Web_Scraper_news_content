from bs4 import BeautifulSoup
import requests
import textwrap

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}
url="https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"

def get_news_articles(url):

    response=requests.get(url,headers=headers)
    if response.status_code!=200:
        print('Failed to load page')
    soup=BeautifulSoup(response.text,'html.parser')

    #extract the title

    title_element=soup.find("h1")
    title=title_element.get_text(strip=True) if title_element else  "Title not found"
    

    #Extract the subtitle

    subtitle_element=soup.find("h2")
    subtitle=subtitle_element.get_text(strip=True) if subtitle_element else "Subtitle not found"
    
    #Extract the article content
    
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('div')] # type: ignore
    
   
    #Extract the article date

    date_element=soup.find('time',{'data-testid': 'timestamp__datePublished'})
    published_date=date_element.get_text(strip=True) if date_element else "Published date not found"
    
    
    # Extract the author

    author_meta_tags=[
        {"name":"article:author"},
        {"name":"author"},
        {"name":"sailthru.author"},
        {"name":"author_name"},
        {"property": "og:article:author"},
        {"property": "byline"},
        {"name": "byline"},
    ]
    author=None
    for tag in author_meta_tags:
        author_element = soup.find("meta", attrs=tag) # type: ignore
        if author_element and author_element.get("content"):# type: ignore
            author = author_element["content"].strip()  # type: ignore
            break
    
    #Wrap each paragraph individually
    wrapped_paragraphs = []
    for paragraph in paragraphs:
        wrapped_paragraph=textwrap.fill(paragraph,width=120)
        wrapped_paragraphs.append(wrapped_paragraph)
    
    article_text="\n".join(wrapped_paragraphs)

    article_info = f"""
    Title: {title}
    Subtitle: {subtitle}
    Author: {author}
    Published Date: {published_date}

    Article:
    {article_text}
    """
    return article_info

 



print(get_news_articles(url))