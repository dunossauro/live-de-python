from pyrate_limiter import limiter_factory
from pyrate_limiter.extras.httpx_limiter import RateLimiterTransport
from pyrate_limiter.abstracts.rate import Duration
import httpx

limiter = limiter_factory.create_inmemory_limiter(
    rate_per_duration=10, duration=Duration.DAY,
)  # Um request por segundo

limiter_transport = RateLimiterTransport(limiter=limiter)

with httpx.Client(transport=limiter_transport) as client:
    print(client.get('https://dunossauro.com'))


logger.info('request!')
