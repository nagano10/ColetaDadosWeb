import csv
import os
import logging

class NewsSaver:
    def __init__(self, output_dir="output", filename="news_data.csv"):
        self.output_dir = output_dir
        self.filename = filename

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def get_unique_filepath(self, base_filepath):

        if not os.path.exists(base_filepath):
            return base_filepath

        filename, ext = os.path.splitext(base_filepath)
        counter = 1

        while True:
            new_filepath = f"{filename}({counter}){ext}"
            if not os.path.exists(new_filepath):
                return new_filepath
            counter += 1

    def save_to_csv(self, news_list):
        if not news_list:
            logging.info("Nenhuma noticia para salvar.")
            return

        base_filepath = os.path.join(self.output_dir, self.filename)
        filepath = self.get_unique_filepath(base_filepath)

        headers = news_list[0].keys()

        try:
            with open(filepath, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(news_list)

            logging.info(f"Arquivo CSV salvo com sucesso em: {filepath}")

        except Exception as e:
            logging.error(f"Falha ao salvar arquivo: {e}")
