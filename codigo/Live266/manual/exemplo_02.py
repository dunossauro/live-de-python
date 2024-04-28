from logging import INFO, Filter
from loguru import logger

from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import (
    BatchLogRecordProcessor,
    ConsoleLogExporter,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

resource = Resource({SERVICE_NAME: 'LogAPP'})
provider = LoggerProvider(resource=resource)
processor = BatchLogRecordProcessor(ConsoleLogExporter())
provider.add_log_record_processor(processor)

set_logger_provider(provider)


class RemoveExtra(Filter):
    def filter(self, record):
        del record.extra
        return True

handler = LoggingHandler(level=INFO, logger_provider=provider)
handler.addFilter(RemoveExtra())

# OTel Handler
logger.add(handler, level='DEBUG', serialize=True)

logger.critical('aaaaaaaa')
