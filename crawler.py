import requests
import csv
from bs4 import BeautifulSoup
# urljoin baut weiterführende links aus reletiven pfadangaben zusammen
# angegeben muss der initiale link, wobei nur die base als root genommen wird unabhängig ob die url die erste Seite ist
# oder bereits tiefer in der Hierarchie
from urllib.parse import urljoin

# um eine Wartezeit zwischen den einzelnen Durchläufen einer Schleife zu definieren, muss Modul "tine" eingebunden werden
import time

class CrawledArticle:
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image



class ArticleFetcher:
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        articles = []
        while True:
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            # für alle Elemente der Klasse "card" wird eine Schleife erzeugt
            next_page = doc.select_one(".navigation .btn-primary")
            # print(next_page)
            for element in doc.select(".card"):
                # die Klassenbezeichnung in der Schleife bezieht sich nur auf Elemente innerhalb der Schleifendefinition
                # (Klasse "card" in dem Beispiel)
                emoji = element.select_one(".emoji").text
                content = element.select_one(".card-text").text
                # mehrere span Elemente in .card-title
                # mit "select" als Liste ausgeben und entsprechendes Element als Index definieren. .text nur Inhalt ausgeben
                title = element.select(".card-title span")[1].text
                image = urljoin(url, element.select_one("img").attrs["src"])
                # Objekt mit jedem Scheifendurchlauf an Liste anhängen, wodurch man die einzelnen Ergebnisse außerhalb der
                # Schleife benutzen kann
                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)

                # Außerhalb der Schleife müssen die Ergebnisse jedes Durchlaufs an eine Liste gehängt werden
                # geht so nur mit jedem Schleifendurchlauf
            # print(next_page.attrs["href"])

            # Prüfung ob es die Referent in next_page.attr["href"] gibt, BEVOR mit dem Objekt gearbeitet wird
            # Sonst führt dies zum Fehler "AttributeError: 'NoneType' object has no attribute 'attrs'"
            if next_page is None:
                with open("crawler.csv", "w", newline = "", encoding = "utf-8") as file:
                    writer = csv.writer(file, dialect = "excel-tab", delimiter = ";", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                    for element in articles:
                        writer.writerow([element.emoji, element.title, element.image, element.content])
                return True
            else:
                url = urljoin(url, next_page.attrs["href"])

class FetcherOutput:




ausgabe = ArticleFetcher()
ausgabe_liste = ausgabe.fetch()

# print(ausgabe.fetch()[0].title)

# for element in ausgabe_liste:
#     print(element.emoji + " : " + element.title)

# for element in range (0, len(ausgabe.fetch())):
#     print(ausgabe.fetch()[element].title)