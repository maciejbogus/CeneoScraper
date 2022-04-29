from urllib import response
from bs4 import BeautifulSoup
import requests
import json

url = "https://www.ceneo.pl/91714422#tab=reviews"
all_opinions = []

while(url):
    response = requests.get(url)
    # print(response.status_code) // jak 200 to działa

    page = BeautifulSoup(response.text, "html.parser")

    opinions = page.select("div.js_product-review")

    for  opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            recomendation = opinion.select_one("span.user-post__author-recomendation > em").get_text()
        except AttributeError:
            recomendation = None
        stars = opinion.select_one("span.user-post__score-count").get_text()
        content = opinion.select_one("div.user-post__text").get_text()

        usefull = opinion.select_one('span[id^="votes-yes"]').get_text().strip()
        useless = opinion.select_one('span[id^="votes-no"]').get_text().strip()

        publish_date = purchase_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]

        try:
            purchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
        except TypeError:
            purchase_date=None

        pros = opinion.select("div[class$=\"positives\"]~ div.review-feature__item")
        pros = [item.get_text() for item in pros]

        cons = opinion.select('div[class$=\"negatives\"]~ div.review-feature__item')
        cons = [item.get_text() for item in cons]

        single_option = {
            "opinion_id" : opinion_id,
            "author" : author,
            "recomendation" : recomendation,
            "stars" : stars,
            "content" : content,
            "pros" : pros,
            "cons" : cons,
            "usefull": usefull,
            "useless": useless,
            "publish_date" : publish_date,
            "purchase_date" : purchase_date
        }
        all_opinions.append(single_option)
    try:
        url = "https://www.ceneo.pl" + page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None

with open("opinions\96693065.txt", "w", encoding="UTF-8") as file:
    json.dump(all_opinions, file, indent=4, ensure_ascii=False)