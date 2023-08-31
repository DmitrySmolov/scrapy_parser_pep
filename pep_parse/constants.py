from datetime import datetime as dt
from pathlib import Path

from pep_parse.settings import RES_FILE_FORMAT

BASE_DIR = Path(__file__).parent.parent

MAIN_PEPS_DOMAIN = 'peps.python.org'
MAIN_PEPS_URL = 'https://' + MAIN_PEPS_DOMAIN + '/'

STATUS_SUM_CSV_NAME = ''.join((
    'status_summary_',
    str(dt.now().strftime('%Y-%m-%d_%H-%M-%S')),
    f'.{RES_FILE_FORMAT}'
))

# шаблоны поиска номера и имени PEP в статье каждого PEP
PEP_NUM_NAME_PATTERN = r'PEP (?P<number>\d+) – (?P<name>.+)'
PEP_NUM_PATTERN = r'PEP (?P<number>\d+) –'
PEP_NUM_IN_URL_PATTERN = r'pep-(\d+)/$'


class CssSelector:
    PEPS = 'section[id="numerical-index"] tbody tr[class^="row-"]'
    PEP_LINKS = 'a::attr(href)'
    TITLE = 'h1.page-title::text'


class XpathSelector:
    STATUS = (
        "//dt[contains(., 'Status')]/following-sibling::dd[1]/abbr/text()"
    )
