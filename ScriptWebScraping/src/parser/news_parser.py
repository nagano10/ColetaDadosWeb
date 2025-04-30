import logging

class NewsParser:
    def parse_news(self, raw_news_list):
        parsed_news_list = []

        for news in raw_news_list:

            try:

                parsed_news = {
                    'title': news.get('title', '').strip(),
                    'summary': news.get('summary', '').strip(),
                    'link': news.get('link', '').strip(),
                    'publication_last_update': news.get('publication_last_update', '').strip()
                }

                parsed_news_list.append(parsed_news)

            except Exception as e:
                logging.error(f"Falha ao tratar dados: {e}")

        return parsed_news_list