import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.vedantcomputers.com/pc-components/graphics-card?limit=100"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

all_cards = soup.find_all("div", class_="caption")

cards = []

for card in all_cards:
    row_header = ["Name", "Model No", "Price"]
    name = card.find("div", class_="name").text
    model_name = card.find("span", class_="stat-1")
    price = card.find("span", class_="price-normal")
    if model_name is not None and price is not None:
        model_name = model_name.find_all("span")[1].text
        price = price.text
        cards.append(dict({"name":name, "model_name":model_name, "price":price}))

with open("graphics_card_list", "w") as f:
    write = csv.writer(f)
    write.writerow(row_header)
    for card in cards:
        write.writerow([card.get("name"), card.get("model_name"), float(card.get("price")[1:].replace(',',''))])
    
