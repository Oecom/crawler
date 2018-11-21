import requests
from io import BytesIO
from PIL import Image
import simplejson as json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#
# # URL mit get (GET):
# params = {"q" : "pizza"}
# r1 = requests.get("https://www.bing.com/search?", params=params)
# print("Status:", r1.status_code)
# print("Encoding:", r1.encoding)
# print("URL:", r1.url)
# # print("Text:", r1.text)
#
# file = open("./crawler2.html", "w+", encoding="utf-8")
# file.write(r1.text)
#
#
# # Pillow und BytesIO Beispiel -> beide importieren (line 2, 3)
# # Bild soll per requests angefordert und im Nachgang weiterverarbeitet werden
#
# r2 = requests.get("https://s3.amazonaws.com/peoplepng/wp-content/uploads/2018/07/04095156/Stone-PNG-Transparent-Image-2-1024x971.png")
# print("Status:", r2.status_code)
# # print("Content:", r2.content)
#
# # r2.content gibt binäre Daten wieder, diese werden durch BytesIO verarbeitet und über Image als Bild konvertiert.
# # r2.text gibt dieselben Daten in Unicode zurück, kann also von Menschen gelesen werden.
#
# image = Image.open(BytesIO(r2.content))
# print(image.size, image.format, image.mode)
#
# # Das Format wird aus der Variable image ausgelesen und beim speichern als Dateityp gesetzt
# path = "./image." + image.format
#
# try:
#     image.save(path, image.format)
# except IOError:
#     print("kann Bild nicht speichern!")
#
# # Mittels http POST wird der key, value an URL geschickt, die genau diese Werte erwartet.
# # Vorher habe ich das Formular angeschaut und wie die Felder heißen, die die keys für POST bilden.
# # Anschließend die Ziel-URL und die key, values aus dem Formular mittels request an Zielseite schicken:
# my_data = {"name" : "Nick", "email" : "nick@example.com"}
# r3 = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)
#
# with open("myfile.html", "w+") as f:
#     f.write(r3.text)
#
# # simplejson als json importieren (siehe Zeile 4)
# # Payload (Daten) erzeugen, die an eine URL gesendet werden sollen
# # Via requests.post die Daten an die Anwendung senden
# url = "https://www.googleapis.com/urlshortener/v1/url"
# payload = {"long_url" : "https://www.hs-bremerhaven.de/start/"}
# headers = {"Content-Type" : "application/json"}
# r4 = requests.post(url, json=payload, headers=headers)
#
# print(json.loads(r4.text)["error"]["code"])
#
# # Headers müssen bspw. beim Senden an eine API mit entsprechendem Inhalt mit übermittelt werden.
# # Im oberen Beispiel wurde der Header content type mit application/json and die API geschickt.
# print(r4.headers)
#
# # BeautifulSoup importieren (line 5), um via request angeforderte Daten aus dem Web zu verarbeiten
# search = input("Enter search term:")
# params5 = {"q" : search}
# url5 = "https://www.bing.com/search"
# r5 = requests.get(url5, params=params5)
# soup = BeautifulSoup(r5.text, "lxml")
# # In results wird das die Suchergebnisse umfassende Element in results gespeichert.
# # Es ist keine Liste nur ein langer String. In Links wird aus dem String mittels soup
# # die Überschrift und der Link des Ergebnisses extrahiert und als Element einer Liste gespeichert.
#
# results = soup.find("ol", {"id" : "b_results"})
# links = results.findAll("li", {"class" : "b_algo"})
#
# print(results)
# print(links)
#
# for element in links:
#     element_text = element.find("a").text
#     element_link = element.find("a").attrs["href"]
#     # Element <p> ist auf dritter Hierarchiestufe in der soup. Da es alleine je Element
#     # vorkommt, kann es direkt angesprochen werden.
#     element_description = element.find("p").text
#
#     # Mit parent gehen wir jeweils eine Hierarchiestufe hoch.
#     # element_description2 = element.find("a").parent.parent.find("p").text
#
#     if element_text and element_link:
#         # print(element_text)
#         print("Desciption:", element_description)
#         # print("Desciption2:", element_description2)
#         print(element_link)
#         print("Parent:", element.find("a").parent)
#
#         children = element.children
#         for child in children:
#             print("Child:", child)
#
#         children2 = element.find("h2")
#         # mit previous_ und next_sibling kann man auf das vorherige oder nächste Element des gleichen Typs zugreifen.
#         # Gibt hier mittlerweile nur ein h2, deshalb funktioniert das Beispiel nicht wie vorgesehen.
#
#         # print("Previous sibling of h2:", children2.previous_sibling)
#         # print("Next sibling of h2:", children2.next_sibling)

# Scrapping Images

# search6 = input("Suchbegriff:")
# print(search6)
# counter6 = 1
# params6 = {"q" : search6}
# url6 = "https://www.bing.com/images/search"
# r6 = requests.get(url6, params=params6)
#
# print("r6:", r6.url)
#
# soup6 = BeautifulSoup(r6.text, "html.parser")
# with open("./soup6.html", "w+", encoding="utf-8") as file6:
#     file6.write(r6.text)
#
# print("soup6:", soup6)
# links6 = soup6.findAll("img", {"class" : "mimg")
#print("links6:", links6)

# for element in links6:
#     img_object6 = requests.get(element.attrs["src"])
#     print(img_object6)
#     title6 = element.attrs["href"].split("/")[-1]
#     print(title6)
#     img6 = Image.open(BytesIO(img_object6.content))
#     img6.save("./scraped_images/" + search6 + counter6, img.format)
#     counter6 += 1

search = input("Suchbegriff:")
params = {"q" : search}
url = "https://www.bing.com/images/search"
r = requests.get(url, params=params)
# print(r.url)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class" : "thumb"})

for item in links:
    img_obj = requests.get(urljoin(url, item.attrs["href"]))
    title = item.attrs["href"].split("/")[-1]
    img = Image.open((BytesIO(img_obj.content)))
    img.save("./scraped_images/" + title. img.format)


