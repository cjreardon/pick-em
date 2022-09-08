from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.pinnacle.com/en/football/nfl/matchups/")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify)