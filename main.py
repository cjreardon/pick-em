from re import L
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.pinnacle.com/en/football/nfl/matchups/')

team_names = driver.find_elements(By.CLASS_NAME, 'style_participant__H8-ku')
odds = driver.find_elements(By.CLASS_NAME, "style_price__15SlF")
filtered = []
odds_map = {}

for j in range(2, len(odds), 6):
    filtered.append(odds[j].text)
    filtered.append(odds[j+1].text)

for k in range(len(team_names)):
    odds_map[team_names[k].text] = filtered[k]

odds_map = sorted(odds_map.items(), key=lambda item: item[1])

for x in odds_map:
    print(x[0] + ": " + x[1])
