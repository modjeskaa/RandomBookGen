import requests
from bs4 import BeautifulSoup
import random

gatunek_URL = {
    "Literatura piękna": "https://lubimyczytac.pl/ksiazki/k/39/literatura-piekna",
    "Klasyka": "https://lubimyczytac.pl/ksiazki/k/44/klasyka",
    "Kryminał, sensacja, thriller": "https://lubimyczytac.pl/ksiazki/k/53/kryminal-sensacja-thriller",
    "Reportaż": "https://lubimyczytac.pl/ksiazki/k/46/reportaz",
    "Biografia, autobiografia, pamiętnik": "https://lubimyczytac.pl/ksiazki/k/40/biografia-autobiografia-pamietnik",
    "Literatura popularnonaukowa": "https://lubimyczytac.pl/ksiazki/k/68/popularnonaukowa",
    "Fantasy, science-fiction": "https://lubimyczytac.pl/ksiazki/k/41/fantasy-science-fiction",
    "Literatura dziecięca": "https://lubimyczytac.pl/ksiazki/k/45/literatura-dziecieca",
    "Komiksy": "https://lubimyczytac.pl/ksiazki/k/110/komiksy",
    "Poezja, dramat, satyra": "https://lubimyczytac.pl/ksiazki/k/111/poezja-dramat-satyra",
    "Sztuka": "https://lubimyczytac.pl/ksiazki/k/86/sztuka",
    "Pozostałe": "https://lubimyczytac.pl/ksiazki/k/109/pozostale"
}

def getRandomBook(url):

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', class_='authorAllBooks__singleTextTitle')
        book_links = [link['href'] for link in links if link['href'].startswith('/ksiazka/')]

        if book_links:
            random_book_link = random.choice(book_links)
            return 'https://lubimyczytac.pl' + random_book_link
        else:
            print("No book links found.")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")


genre_url = gatunek_URL["Fantasy, science-fiction"]
random_book_by_genre_url = getRandomBook(genre_url)
print(random_book_by_genre_url)
