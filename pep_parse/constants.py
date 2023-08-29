from datetime import datetime as dt
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'

MAIN_PEPS_DOMAIN = 'peps.python.org'
MAIN_PEPS_URL = 'https://' + MAIN_PEPS_DOMAIN + '/'

STATUS_SUM_CSV_NAME = (
    'status_summary_' + str(dt.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
)
STATUS_SUM_CSV_PATH = os.path.join(RESULTS_DIR, STATUS_SUM_CSV_NAME)

# шаблон поиска номера и имени PEP в заголовке статьи каждого PEP
PEP_NUM_NAME_PATTERN = r'PEP (?P<number>\d+) – (?P<name>.+)'
