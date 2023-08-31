from collections import Counter
import csv
import os

from scrapy.spiders import Spider

from pep_parse.constants import BASE_DIR, STATUS_SUM_CSV_NAME
from pep_parse.items import PepParseItem
from pep_parse.settings import ENCODING


class PepParsePipeline:

    def __init__(self: 'PepParsePipeline') -> None:
        self.status_summary = Counter()

    def open_spider(self: 'PepParsePipeline', spider: Spider) -> None:
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        status_sum_csv_path = os.path.join(results_dir, STATUS_SUM_CSV_NAME)
        self.summary_file = open(file=status_sum_csv_path, mode='w',
                                 newline='', encoding=ENCODING)
        self.summary_writer = csv.writer(self.summary_file)
        self.summary_writer.writerow(['Статус', 'Количество'])

    def process_item(
        self: 'PepParsePipeline', item: PepParseItem, spider: Spider
    ) -> PepParseItem:
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self: 'PepParsePipeline', spider: Spider) -> None:
        for status, count in self.status_summary.items():
            self.summary_writer.writerow([status, count])
        total_count = sum(self.status_summary.values())
        self.summary_writer.writerow(['Total', total_count])
        self.summary_file.close()
