import requests
from bs4 import BeautifulSoup
import time

# Function to print styled messages
def print_with_style(text, color_code='0A'):
    """Print text with a style (color)."""
    print(f"\033[{color_code}m{text}\033[0m")

# Clear the screen (works in most terminals)
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Header with color
print_with_style("""
 ____   ____ ____      _    ____    __  __ _____
/ ___| / ___|  _ \    / \  |  _ \  |  \/  | ____|
\___ \| |   | |_) |  / _ \ | |_) | | |\/| |  _|  
 ___) | |___|  _ <  / ___ \|  __/  | |  | | |___ 
|____/ \____|_| \_\/_/   \_\_|     |_|  |_|_____|  

⚠️ WARNING: USE THIS SCRIPT RESPONSIBLY ⚠️
    Made by Taha185
""", color_code='1;33')  # Yellow warning message and header

# Main Program
def fetch_page(url):
    """Fetch the HTML content of the page."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.RequestException as e:
        print_with_style(f"Error fetching the page: {e}", color_code='31')  # Red error message
        return None

def parse_page(html_content):
    """Parse the HTML content using BeautifulSoup and extract titles."""
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = [h2.get_text() for h2 in soup.find_all('h2')]  # Example: Extract all h2 titles
    return titles

def main():
    while True:
        # Ask user for URL
        url = input("\nEnter the URL to scrape (or 'exit' to quit): ").strip()

        if url.lower() == 'exit':  # Allow the user to quit the program anytime
            print_with_style("Exited with code 0", color_code='33')  # Yellow message
            break
        
        if not url.startswith(('http://', 'https://')):  # Basic URL validation
            print_with_style("Invalid URL. Please enter a valid URL starting with 'http://' or 'https://'.", color_code='31')
            continue
        
        # Display a loading message
        print_with_style("Fetching and parsing the page...", color_code='36')  # Cyan color
        time.sleep(1)  # Simulate a small delay for effect

        # Fetch and parse the page content
        html_content = fetch_page(url)

        if html_content:
            titles = parse_page(html_content)
            if titles:
                print_with_style("\nTitles found on the page:\n", color_code='32')  # Green color for titles
                for title in titles:
                    print_with_style(f"- {title}", color_code='32')  # Green for each title
            else:
                print_with_style("No titles found on this page.", color_code='33')  # Yellow message
        
        # Ask user if they want to scrape another page
        user_input = input("\nDo you want to scrape another page? (yes/no): ").strip().lower()
        if user_input != 'yes':
            print_with_style("Exited with code 0", color_code='33')  # Yellow message
            break

if __name__ == "__main__":
    main()
