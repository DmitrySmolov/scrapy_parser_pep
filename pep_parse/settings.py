BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ENCODING = 'utf-8'

RES_FILE_FORMAT = 'csv'

ROBOTSTXT_OBEY = True

FEEDS = {
    f'results/pep_%(time)s.{RES_FILE_FORMAT}': {
        'format': RES_FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
        'encoding': ENCODING,
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
