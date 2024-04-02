"""O mínimo necessário para instrumentar manualmente

Obs:
- `resource` é o identificador da nossa aplicação
- Exportação sendo feita de forma periódica (PeriodicExportingMetricReader)
- Exportação sendo feita somente para o terminal (ConsoleMetricExporter)
- `MeterProvider` Junta o exporter com o nosso `resource`
"""
from opentelemetry.metrics import get_meter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

resource = Resource(attributes={SERVICE_NAME: 'meu app'})

reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
meter_provider = MeterProvider(resource=resource, metric_readers=[reader])

print(resource.attributes)

meter = get_meter('meters', meter_provider=meter_provider)

counter = meter.create_counter(
    'contador',
    description='Contagem de coisas!',
    unit='????',
)


counter.add(1, {'dado': 'Alguma coisa!'})

from opentelemetry.metrics import Observation

def callback(observer):
    # coleta algo
    yield Observation(1, {'dado': 'Alguma coisa!'})


async_counter = meter.create_observable_counter(
    'contador asyncrono',
    description='Contagem de coisas assincronamente!',
    unit='???',
    callbacks=[callback]
)

print(meter_provider._meters)
