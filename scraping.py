
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?viewType=listing')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all listings
    listings = soup.find_all('div', class_='css-1ojmxpg e17ey1dw2')
    print(listings)
else:
    print("Failed to retrieve the webpage.")

