import logging
from os import environ
from time import time

from opentelemetry.metrics import get_meter
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.routing import Match

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
meter = get_meter('spam.meter')

req_count = meter.create_counter(
    name='request_counter',
    description='Quantidade total de requests',
)

err_count = meter.create_counter(
    name='error_counter',
    description='Quantidade total de erros',
)

active_count = meter.create_up_down_counter(
    name='active_requests',
    description='Quantidade de requests ativos.',
)

total_time = meter.create_histogram(
    name='total_request_time', description='time to response a request.'
)


class MetricsMeddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app=app)
        self.app_name = environ.get('OTEL_SERVICE_NAME', 'spam')

    def get_path(self, request: Request):
        for route in request.app.routes:
            match_, _ = route.matches(request.scope)
            if match_ == Match.FULL:
                return route.path

        return request.url.path

    async def dispatch(self, request: Request, call_next):
        method = request.method
        base_attributes = {
            'method': method, 'path': self.get_path(request)
        }

        active_count.add(1, attributes=base_attributes)
        start_time = time()

        try:
            response = await call_next(request)
            attributes = base_attributes | {
                'status_code': response.status_code,
            }
            req_count.add(1, attributes=attributes)
        except Exception as e:
            attributes = base_attributes | {
                'exception_type': type(e).__name__,
                'status_code': 500,
            }
            req_count.add(1, attributes=attributes)
            err_count.add(1)
            logger.error('Deu ruim!')
            raise e from None
        finally:
            active_count.add(-1, attributes=base_attributes)
            total_time.record(time() - start_time, attributes=base_attributes)

        return response
