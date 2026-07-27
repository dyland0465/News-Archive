import requests
from src.config import API_KEY, COUNTRY
from src.database import init_db, SaveToDB


def fetchTopHeadlines():
    url = f"https://newsapi.org{COUNTRY}&apiKey={API_KEY}"
    print(f"[API] Fetching top headlines for region: '{COUNTRY}'...")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        print(f"Successfully retrieved {len(articles)} items.")
        return articles
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Failed: {e}")
        return []


def main():
    print("Starting")

    init_db()

    articles = fetchTopHeadlines()

    SaveToDB(articles)

    print("Pipeline execution complete")


if __name__ == "__main__":
    main()
