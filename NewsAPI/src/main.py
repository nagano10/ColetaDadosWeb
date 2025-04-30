from api.api_connector import GNewsAPIConnector
from parser.news_parser import NewsParser
from saver.news_saver import NewsSaver
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    connector = GNewsAPIConnector(query="tecnologia")
    parser = NewsParser()
    saver = NewsSaver()

    try:
        logging.info(f"Coletando noticias da Gnews API")
        raw_news = connector.fetch_news()

        logging.info(f"Noticias coletadas")

        logging.info(f"Tratando noticias")
        parsed_news = parser.parse_news(raw_news)

        logging.info(f"Salvando noticias no CSV")
        saver.save_to_csv(parsed_news)

    except Exception as e:
        logging.error(f"Ocorreu um erro durante a execucao: {e}")

if __name__ == "__main__":
    main()
