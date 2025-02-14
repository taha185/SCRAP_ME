import requests
from bs4 import BeautifulSoup

print("""
 ____   ____ ____      _    ____    __  __ _____
/ ___| / ___|  _ \    / \  |  _ \  |  \/  | ____|
\___ \| |   | |_) |  / _ \ | |_) | | |\/| |  _|
 ___) | |___|  _ <  / ___ \|  __/  | |  | | |___
|____/ \____|_| \_\/_/   \_\_|     |_|  |_|_____|
""")

print("1 to exit, 0 to keep going\n")
user_input = input("Choose option: ")


if user_input == '1':
    print("Exited with code 0")
else:
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
