import logging
import re

from scrapy import Spider

from pep_parse.constants import (CssSelector, MAIN_PEPS_DOMAIN, MAIN_PEPS_URL,
                                 PEP_NUM_IN_URL_PATTERN, PEP_NUM_NAME_PATTERN,
                                 PEP_NUM_PATTERN, XpathSelector)
from pep_parse.items import PepParseItem


class PepSpider(Spider):
    name = 'pep'
    allowed_domains = [MAIN_PEPS_DOMAIN]
    start_urls = [MAIN_PEPS_URL]

    def parse(self, response):
        peps = response.css(CssSelector.PEPS)
        pep_links = [pep.css(CssSelector.PEP_LINKS).get() for pep in peps]
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css(CssSelector.TITLE).get()
        pep_match = re.search(pattern=PEP_NUM_NAME_PATTERN, string=title)
        if pep_match is None:
            pep_match = re.search(pattern=PEP_NUM_PATTERN, string=title)
        if pep_match is None:
            message = (
                f'Заголовок "{title}" не соответствует ожидаемому шаблону для'
                ' парсинга'
            )
            logging.info(msg=message)
            number = re.search(pattern=PEP_NUM_IN_URL_PATTERN,
                               string=response.url)
            name = title
        number = pep_match.group('number')
        if len(pep_match.groups()) == 2:
            name = pep_match.group('name')
        else:
            name = title
        status = response.xpath(XpathSelector.STATUS).get()
        yield PepParseItem(number=number, name=name, status=status)
