from scraper.news_scraper import NewsScraper
from parser.news_parser import NewsParser
from saver.news_saver import NewsSaver

def main():

    url = "https://g1.globo.com/"

    scraper = NewsScraper(url)
    parser = NewsParser()
    saver = NewsSaver()

    try:
        print("[INFO] Iniciando driver")
        scraper.start_driver()

        print("[INFO] Coletando noticias")
        raw_news = scraper.collect_news()

        print(f"[INFO] {len(raw_news)} noticias coletadas")

        print("[INFO] Tratando noticias")
        parsed_news = parser.parse_news(raw_news)

        print("[INFO] Salvando noticias no csv")
        saver.save_to_csv(parsed_news)

    except Exception as e:
        print("[ERROR] Ocorreu um erro: {e}")

    finally:
        print("[INFO] Fechando driver")
        scraper.close_driver()

if __name__ == "__main__":
    main()