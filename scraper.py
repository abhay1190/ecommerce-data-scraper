import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/"

books = []

for page in range(1, 6):  # scrape first 5 pages
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())  # Print the HTML content of the page for debugging
    articles = soup.find_all("article", class_="product_pod")
    # print(articles)  # Print the list of items for debugging

    for article in articles:
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text
        availability = article.find("p", class_="instock availability").text.strip()
        rating = article.p["class"][1]

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

df = pd.DataFrame(books)
df.to_csv("output.csv", index=True)

print("Scraping completed. Data saved to output.csv")
