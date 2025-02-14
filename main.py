import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def parse_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Example: Extract all the titles of the articles
    titles = [h2.get_text() for h2 in soup.find_all('h2')]
    return titles

def main():
    url = input("Enter the URL to scrape: ")
    html_content = fetch_page(url)

    if html_content:
        titles = parse_page(html_content)
        for title in titles:
            print(title)

if __name__ == "__main__":
    main()
