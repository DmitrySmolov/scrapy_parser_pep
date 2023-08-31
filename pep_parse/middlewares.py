from typing import Any, Generator, Iterable, Optional

from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.http import Request, Response
from scrapy.spiders import Spider


class PepParseSpiderMiddleware:
    @classmethod
    def from_crawler(
        cls: 'PepParseSpiderMiddleware', crawler: Crawler
    ) -> 'PepParseSpiderMiddleware':
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(
        self: 'PepParseSpiderMiddleware', response: Response,
        spider: Spider
    ) -> None:
        return None

    def process_spider_output(
        self: 'PepParseSpiderMiddleware', response: Response,
        result: Iterable[Any], spider: Spider
    ) -> Generator:
        for i in result:
            yield i

    def process_spider_exception(
        self: 'PepParseSpiderMiddleware', response: Response,
        exception: Exception, spider: Spider
    ) -> Optional[Any]:
        pass

    def process_start_requests(
        self: 'PepParseSpiderMiddleware', start_requests: Iterable[Request],
        spider: Spider
    ) -> Generator:
        for r in start_requests:
            yield r

    def spider_opened(
        self: 'PepParseSpiderMiddleware', spider: Spider
    ) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:
    @classmethod
    def from_crawler(
        cls: 'PepParseDownloaderMiddleware', crawler: Crawler
    ) -> 'PepParseDownloaderMiddleware':
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(
        self: 'PepParseDownloaderMiddleware', request: Request, spider: Spider
    ) -> None:
        return None

    def process_response(
        self: 'PepParseDownloaderMiddleware', request: Request,
        response: Response, spider: Spider
    ) -> Response:
        return response

    def process_exception(
        self: 'PepParseDownloaderMiddleware', request: Request,
        exception: Exception, spider: Spider
    ) -> Optional[Any]:
        pass

    def spider_opened(
        self: 'PepParseDownloaderMiddleware', spider: Spider
    ) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
