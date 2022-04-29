# CeneoScraper

|SKŁADOWA|SELEKTOR|NAZWA ZMIENNEJ|TYP ZMIENNEJ|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|obj
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|str
|autor opinii|span.user-post__author-name|author|str
|rekomendacja|span.user-post__author-recomendation > em|recomendation|str
|liczba gwiazdek|span.user-post__score-count|stars|string
|treść opinii|div.user-post__text|content|str
|lista zalet|div[class?="positives"]~ div.review-feature__item|pros|list
|lista wad|div[class?="negatives"]~ div.review-feature__item|cons|list
|dla ilu osob przydatna|span[id^="votes-yes"]|usefull|int
|dla ilu osob nieprzydatna|span[id^="votes-no"]|useless|int
|data wystawienia opinii|user-post__published > time:nth-child(1)["datetime]|publish_date|date
|data zakupu|user-post__published > time:nth-child(1)["datetime]|purchase_date|date