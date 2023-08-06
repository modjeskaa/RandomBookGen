from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import requests

def getBookUrls():
    url = "https://lubimyczytac.pl/top100"
    response = urlopen(url)
    html_code = response.read().decode("utf-8")
    soup = BeautifulSoup(html_code, "html.parser")
    forms = soup.find_all("form", class_="formToHref authorAllBooks__singleImgWrap authorAllBooks__singleImgWrap__hovered")
    actions = [form["action"] for form in forms]
    return actions

def pick_random():
    book_urls = getBookUrls()
    random_url = random.choice(book_urls)
    return random_url

def returnRandomBookURL():
    random_book_url = pick_random()
    url = "https://lubimyczytac.pl"
    result = f"{url}{random_book_url}"
    return result

def getAuthorTitlePic(url):  
    response = requests.get(url)
    html_code = response.text
    soup = BeautifulSoup(html_code, "html.parser")

    title_container = soup.find("div", class_="title-container")
    if title_container:
        title = title_container.h1.text.strip()
    else:
        title = "Brak tytułu."

    author_element = soup.find("span", class_="author pb-2")
    if author_element:
        author_name = author_element.a.text.strip()
    else:
        author_name = "Autor nie znaleziony."

    image_element = soup.find("img", class_="img-fluid")
    if image_element:
        image_src = image_element["src"]
    else:
        image_src = "Brak zdjęcia."

    return title, author_name, image_src


random_book_url = returnRandomBookURL()
author_and_title_and_image = getAuthorTitlePic(random_book_url)
