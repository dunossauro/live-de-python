import logging

# pip install opentelemetry-distro

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

handler = LoggingHandler(
    level=logging.INFO,
    logger_provider=provider
)

logger = logging.getLogger()

# OTel Handler
logger.addHandler(handler)

# Default Handler
# logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.DEBUG)

logger.critical('aaaaaaaa')
