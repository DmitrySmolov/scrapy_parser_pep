from collections import Counter
import csv

from pep_parse.constants import BASE_DIR, STATUS_SUM_CSV_PATH
from pep_parse.settings import ENCODING


class PepParsePipeline:

    def __init__(self):
        self.status_summary = Counter()

    def open_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        self.summary_file = open(file=STATUS_SUM_CSV_PATH, mode='w',
                                 newline='', encoding=ENCODING)
        self.summary_writer = csv.writer(self.summary_file)
        self.summary_writer.writerow(['Статус', 'Количество'])

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        self.summary_file = open(file=STATUS_SUM_CSV_PATH, mode='w',
                                 newline='', encoding=ENCODING)
        self.summary_writer = csv.writer(self.summary_file)
        self.summary_writer.writerow(['Статус', 'Количество'])
        for status, count in self.status_summary.items():
            self.summary_writer.writerow([status, count])
        total_count = sum(self.status_summary.values())
        self.summary_writer.writerow(['Total', total_count])
        self.summary_file.close()
