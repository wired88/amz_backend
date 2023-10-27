import requests
from bs4 import BeautifulSoup
import os


# Funktion, um die Suchergebnisse von Amazon zu durchsuchen
def search_amazon(query01, header):
    search_url = f"https://www.amazon.de/s?k={query01}"
    response = requests.get(search_url, headers=header)
    print(response.status_code, "response: ", response)
    if response.status_code == 200 or response.status_code == 201:
        return response.text
    else:
        print(response.status_code, response.cookies.values(), "Error while handling the searchrequest.")
        return None


# Funktion, um Top-Produkte aus den Suchergebnissen zu extrahieren
def extract_top_products(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    product_elements = soup.find_all('div', class_='sg-col-inner')# Die ersten 10 Produkteproduct_
    elements = soup.find_all('div', class_='a-link-normal s-no-outline')# Die ersten 10 Produkte
    print("################################################################", elements, "#################################################################")
    for product_element in product_elements[:10]:  # Die ersten 10 Produkte
        print("Product Element: ", product_element)
        product_data = {}
        product_title = product_element.find('span', class_='a-text-normal')
        product_url = product_title.find('a')['href']
        product_data['title'] = product_title.text.strip()
        product_data['url'] = product_url
        products.append(product_data)
    return products


# Funktion, um Partnerlinks zu extrahieren
def extract_partner_links(product):
    product_url = "https://www.amazon.de" + product['url']
    print("p:", product_url)
    response = requests.get(product_url)
    print("r:", response)
    if response.status_code == 200 or response.status_code == 201:
        soup = BeautifulSoup(response.text, 'html.parser')
        partner_links = []
        many_tags = soup.find_all('a')
        for single_tag in many_tags:
            if 'href' in single_tag.attrs:
                link = single_tag['href']
                description = single_tag.text.strip()
                partner_link = {
                    'description': description,
                    'link': link
                }
                partner_links.append(partner_link)

        return partner_links
    else:
        print("Fehler beim Abrufen des Produktseiteninhalts.")
        return []


search_params = [
    "iphone",
    "smartphone",
    "smartphone",
    "xbox",
    "playstation 5",
    "smartphone",
    "smartphone",
    "smartphone",
    "smartphone",
    "cyberpunk 2077",
    "Assassin's Creed Mirage",
    "Forza Motorsport 2023",
    "Der Herr der Ringe: Return to Moria",
    "Ghostrunner 2",
    "RoboCop: Rogue City ",
    "Call of Duty Modern Warfare 3 ",
    "Avatar - Frontiers of Pandora",
    "Crimson Desert",
    "Alan Wake 2",
]

# later
# "Gta6",

search_query = [{"key": value} for value in search_params]

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",
        "Proxy": "89.247.169.77"
    }

if __name__ == "__main__":
    for query in search_params:
        print(query)
        search_results = search_amazon(query, headers)
        if search_results:
            top_products = extract_top_products(search_results)
            for i, product in enumerate(top_products):
                print(f"\nProdukt {i + 1}:")
                print(f"Titel: {product['title']}")
                print(f"URL: {product['url']}")
                partner_links = extract_partner_links(product)
                if partner_links:
                    print("Partnerlinks:")
                    for link in partner_links:
                        print(f"{link['description']}: {link['link']}")


                else:
                    print("Keine Partnerlinks gefunden.")
        else:
            print("Keine Suchergebnisse gefunden.")
