import re

from scrapy import Spider
from scrapy.exceptions import DropItem

from pep_parse.constants import (MAIN_PEPS_DOMAIN, MAIN_PEPS_URL,
                                 PEP_NUM_NAME_PATTERN)
from pep_parse.items import PepParseItem


class PepSpider(Spider):
    name = 'pep'
    allowed_domains = [MAIN_PEPS_DOMAIN]
    start_urls = [MAIN_PEPS_URL]

    def parse(self, response):
        peps = response.css('section[id="numerical-index"]').css('tbody').css(
            'tr[class^="row-"]'
        )
        pep_links = [pep.css('a::attr(href)').get() for pep in peps]
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        pep_match = re.search(pattern=PEP_NUM_NAME_PATTERN, string=title)
        if pep_match is None:
            pep_match = re.search(r'PEP (?P<number>\d+) –', title)
        if pep_match is None:
            raise DropItem(
                f'Заголовок "{title}" не соответствует ожидаемому шаблону для'
                ' парсинга'
            )
        number = pep_match.group('number')
        if len(pep_match.groups()) == 2:
            name = pep_match.group('name')
        else:
            name = ''
        status = response.xpath(
            "//dt[contains(., 'Status')]/following-sibling::dd[1]/abbr/text()"
        ).get()
        yield PepParseItem(number=number, name=name, status=status)
