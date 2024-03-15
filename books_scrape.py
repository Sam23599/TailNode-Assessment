import requests
from bs4 import BeautifulSoup
import pymongo

# Function to scrape books data 
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books_data = []

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.p['class'][1]
        books_data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })
    
    return books_data

# Function to store scraped data in MongoDB database
def store_in_database(data):
    mongo_client = pymongo.MongoClient("mongodb+srv://satyamvirat:mnVq8nXwhXZB70mz@cluster0.9flhz7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = mongo_client["books"]
    collection = db["books_scrape"]

    collection.insert_many(data)

    print("Books data stored in MongoDB.")

# Main function to process scraping and storing 
def main():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    total_pages = 50
    
    all_books_data = []

    for page in range(1, total_pages + 1):
        url = base_url.format(page)
        books_data = scrape_books(url)
        all_books_data.extend(books_data)

    store_in_database(all_books_data)

if __name__ == "__main__":
    main()
