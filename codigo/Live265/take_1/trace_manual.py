from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import get_tracer, set_tracer_provider

resource = Resource({SERVICE_NAME: 'blah'})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint='http://localhost:4317', insecure=True)
)
#processor = BatchSpanProcessor(
#    ConsoleSpanExporter()
#)
provider.add_span_processor(processor)
set_tracer_provider(provider)
tracer = get_tracer(__name__)


def xpto():
    return 1/0

@tracer.start_as_current_span('fazendo algo')
def teste_spam():
    return xpto()


with tracer.start_as_current_span(
    'test', attributes={'batatinhas': 'fritas'}
) as span:
    span.add_event(
        'Um evento bacana!',
        attributes={'batatinhas': 'Menti, são cozindas!'}
    )
    teste_spam()
