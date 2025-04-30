import os
import requests
import time
import logging
from dotenv import load_dotenv

load_dotenv()

class GNewsAPIConnector:

    def __init__(self, query="technology", lang="pt", max_retries=3, delay=2):

        self.api_key = os.getenv("GNEWS_API_KEY")
        print(f"[DEBUG] API KEY: {self.api_key}")

        self.base_url = "https://gnews.io/api/v4/search"
        self.query = query
        self.lang = lang
        self.max_retries = max_retries
        self.delay = delay

    def fetch_news(self):
        params = {
            "q": self.query,
            "lang": self.lang,
            "token": self.api_key,
            "max": 50
        }

        for attempt in range(1, self.max_retries + 1):
            try:
                logging.info(f"Tentativa {attempt} - Requisicao para GNews API")
                response = requests.get(self.base_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                return data.get("articles", [])
            except requests.exceptions.RequestException as e:
                logging.error(f"Erro na tentativa {attempt} = Requisicao para Gnews API")
                time.sleep(self.delay)

        raise Exception("Falha ao conectar com a GNews API apos multiplas tentaivas.")