import requests
import matplotlib.pyplot as plt
from datetime import datetime

def get_show_info(show_name):
    url = f"https://api.trakt.tv/search/show?query={show_name}&extended=full"
    headers = {
        "Content-Type": "application/json",
        "trakt-api-version": "2",
        "trakt-api-key": "06f5e05e-70cf-4860-88cb-69f841ebdfc3"  # Replace with your Trakt API key
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        show_info = response.json()
        return show_info[0]  # Assuming the first search result is the correct show
    except requests.exceptions.RequestException as e:
        print("Error fetching show information:", e)
        return None

def get_show_favorites(show_id):
    current_year = datetime.utcnow().year
    favorites_data = []
    for i in range(5):
        year = current_year - i
        url = f"https://api.trakt.tv/shows/{show_id}/stats/watched/yearly/{year}"
        headers = {
            "Content-Type": "application/json",
            "trakt-api-version": "2",
            "trakt-api-key": "06f5e05e-70cf-4860-88cb-69f841ebdfc3"  # Replace with your Trakt API key
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            favorites_count = response.json()["watcher_count"]
            favorites_data.append((year, favorites_count))
        except requests.exceptions.RequestException as e:
            print(f"Error fetching favorites data for year {year}:", e)
    return favorites_data

def plot_favorites_data(favorites_data, show_name):
    years = [data[0] for data in favorites_data]
    favorites_count = [data[1] for data in favorites_data]

    plt.figure(figsize=(10, 6))
    plt.plot(years, favorites_count, marker='o')
    plt.title(f"Favorites of '{show_name}' Over the Past Five Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Favorites")
    plt.grid(True)
    plt.xticks(years)
    plt.tight_layout()
    plt.show()

def main():
    show_name = "how i met your mother"
    show_info = get_show_info(show_name)
    if show_info:
        show_id = show_info["show"]["ids"]["trakt"]
        favorites_data = get_show_favorites(show_id)
        if favorites_data:
            plot_favorites_data(favorites_data, show_name)

if __name__ == "__main__":
    main()
