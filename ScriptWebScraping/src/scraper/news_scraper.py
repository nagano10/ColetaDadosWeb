import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class NewsScraper:
    def __init__(self, url):

        self.url = url
        self.driver = None

    def start_driver(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def collect_news(self):

        retries = 3
        delay_between_retries = 2

        for attempt in range(1, retries +1):

            try:

                self.driver.get(self.url)
                try:

                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.feed-post-body"))
                    )

                except Exception as e:

                    logging.error(f"Timeout esperando artigos carregarem: {e}")

                break

            except Exception as e:
                logging.error(f"Tentativa {attempt} falhou ao acessar a pagina: {e}")
                time.sleep(delay_between_retries)

        else:
            logging.error("Falha ao acessar a pagina apos multiplas tentativas.")
            return[]

        logging.info("Pagina acessada com sucesso.")

        news_list = []

        articles = self.driver.find_elements(By.CSS_SELECTOR, "div.feed-post-body")

        for article in articles:

            try:

                title = article.find_element(By.CSS_SELECTOR, ".feed-post-link").text
                link = article.find_element(By.CSS_SELECTOR, ".feed-post-link").get_attribute("href")

                try:

                    summary_element = article.find_element(By.CSS_SELECTOR, ".feed-post-body-resumo")
                    summary = summary_element.text.strip()

                except:

                    try:

                        related_items = article.find_elements(By.CSS_SELECTOR, ".bstn-relateditem")
                        related_texts = [item.text.strip() for item in related_items if item.text.strip() != ""]
                        summary = " | ".join(related_texts)

                    except:

                        summary = ""

                try:

                    publication_date_element = article.find_element(By.CSS_SELECTOR, ".feed-post-datetime")
                    publication_date_text = publication_date_element.text.strip()

                    if "há" in publication_date_text.lower():

                        publication_date_text = publication_date_text.lower()

                        if "hora" in publication_date_text:
                            hours_ago = int(publication_date_text.split()[1])
                            publication_datetime = datetime.now() - timedelta(hours=hours_ago)

                        elif "minuto" in publication_date_text:

                            minutes_ago = int(publication_date_text.split()[1])
                            publication_datetime = datetime.now() - timedelta(minutes=minutes_ago)

                        else:

                            publication_datetime = datetime.now()

                        publication_last_update = publication_datetime.strftime("%Y-%m-%d %H:%M:%S")

                    else:

                        publication_last_update = publication_date_text

                except:
                    publication_last_update = ""

                news_list.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "publication_last_update": publication_last_update,
                    "source": "G1"
                })
            except Exception as e:
                logging.error(f"Erro ao coletar uma noticia: {e}")

        return news_list

    def close_driver(self):
        if self.driver:
            self.driver.quit()