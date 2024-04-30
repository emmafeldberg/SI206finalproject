import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime

def get_show_info(show_name):
    url = f"https://www.imdb.com/find?q={show_name}&s=tt&ttype=tv&ref_=fn_tv"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        result_text = soup.find('td', class_='result_text')
        if result_text:
            first_result = result_text.find('a')
            if first_result:
                show_url = "https://www.imdb.com" + first_result['href']
                return show_url
    except requests.exceptions.RequestException as e:
        print("Error fetching show information:", e)
    return None


def get_show_favorites(show_url):
    favorites_data = []
    try:
        response = requests.get(show_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        ratings_chart = soup.find('div', class_='seasons-and-year-nav')
        if ratings_chart:
            ratings_years = ratings_chart.find_all('a')
            for year in ratings_years:
                year_text = year.text.strip()
                if year_text.isdigit():
                    year_int = int(year_text)
                    favorites_data.append((year_int, 0))  # Placeholder for now
    except requests.exceptions.RequestException as e:
        print("Error fetching favorites data:", e)
    return favorites_data

def plot_favorites_data(favorites_data, show_name):
    years = [data[0] for data in favorites_data]
    favorites_count = [data[1] for data in favorites_data]

    plt.figure(figsize=(10, 6))
    plt.plot(years, favorites_count, marker='o')
    plt.title(f"Favorites of '{show_name}' Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Favorites")
    plt.grid(True)
    plt.xticks(years)
    plt.tight_layout()
    plt.show()

def main():
    show_name = "how i met your mother"
    show_url = get_show_info(show_name)
    if show_url:
        favorites_data = get_show_favorites(show_url)
        if favorites_data:
            plot_favorites_data(favorites_data, show_name)

if __name__ == "__main__":
    main()



import unittest
from __main__ import get_show_info, get_show_favorites

class TestShowInfo(unittest.TestCase):
    def test_get_show_info(self):
        # Test case when the show is found on IMDb
        show_name = "how i met your mother"
        show_url = get_show_info(show_name)
        self.assertIsNotNone(show_url)

        # Test case when the show is not found on IMDb
        show_name = "nonexistent show"
        show_url = get_show_info(show_name)
        self.assertIsNone(show_url)

class TestShowFavorites(unittest.TestCase):
    def test_get_show_favorites(self):
        # Test case when valid show URL is provided
        show_url = "https://www.imdb.com/title/tt0460649/"
        favorites_data = get_show_favorites(show_url)
        self.assertTrue(favorites_data)  # Assuming data is retrieved successfully

        # Test case when invalid show URL is provided
        show_url = "https://www.imdb.com/title/tt0000000/"
        favorites_data = get_show_favorites(show_url)
        self.assertFalse(favorites_data)  # Assuming data retrieval fails

if __name__ == '__main__':
    unittest.main()



