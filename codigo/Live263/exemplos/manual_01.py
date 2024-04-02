"""O mínimo necessário para instrumentar manualmente com HTTP

Obs:
- `resource` é o identificador da nossa aplicação
- Exportação sendo feita de forma periódica (PeriodicExportingMetricReader)
- Exportação sendo feita somente para o rede (OTLPMetricExporter)
- `MeterProvider` Junta o exporter com o nosso `resource`
"""
from opentelemetry.exporter.otlp.proto.http.metric_exporter import (
    OTLPMetricExporter,
)
from opentelemetry.metrics import get_meter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

COLECTOR_METRICS_HTTP_ENDPOINT = 'http://0.0.0.0:4318/v1/metrics'

resource = Resource(attributes={SERVICE_NAME: 'meu app'})

reader = PeriodicExportingMetricReader(
    OTLPMetricExporter(endpoint=COLECTOR_METRICS_HTTP_ENDPOINT)
)
meter_provider = MeterProvider(resource=resource, metric_readers=[reader])

meter = get_meter('meters', meter_provider=meter_provider)

counter = meter.create_counter('contador', description='Contagem de coisas!')


counter.add(1, {'dado': 'Alguma coisa!'})
