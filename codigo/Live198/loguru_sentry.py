from logging import DEBUG
from loguru import logger
from sentry_sdk import init
from sentry_sdk.integrations.logging import LoggingIntegration, EventHandler


init(
   dsn=''
    integrations=[LoggingIntegration(level=None, event_level=None)]
)  # Inicia o sentry

logger.add(
    EventHandler(level=DEBUG), format="{time} {level} {message}",
)  # Adiciona o sentry ao loguru

# Logando
logger.debug("A")
logger.info("b")
logger.error("C", extra=dict(bar=43))
logger.exception("d")
