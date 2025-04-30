import logging

class NewsParser:
    def parse_news(self, raw_news_list):
        parsed_news_list = []

        for news in raw_news_list:
            try:
                parsed_news = {
                    'title': news.get('title', '').strip(),
                    'summary': news.get('description', '').strip(),
                    'link': news.get('url', '').strip(),
                    'publication_last_update': news.get('publishedAt', '').strip()
                }

                parsed_news_list.append(parsed_news)

            except Exception as e:
                logging.error(f"Falha ao tratar dados: {e}")

        return  parsed_news_list