from csv import DictWriter
from dataclasses import asdict
from logging import getLogger

from celery import Celery
from celery.signals import worker_process_init
from minio import Minio
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry.trace import get_tracer
from sqlalchemy import select

from .database import Session, Task

logger = getLogger()
tracer = get_tracer('tracer')


@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    CeleryInstrumentor().instrument()


app = Celery('tasks', broker='amqp://coelho')


client = Minio(
    'cegonha:9000',
    access_key='hzrxArkoc19Gqe5hg4rq',
    secret_key='aP82Se6XN6wcfD4NXiigN4Dl2vcB0afrVgKGJo3X',
    secure=False,
)


@tracer.start_as_current_span('Escrevendo no arquivo')
def _generate_csv(data):
    with open('file.csv', 'w') as file:
        d = DictWriter(file, asdict(data[0]).keys())
        for result in data:
            d.writerow(asdict(result))


@tracer.start_as_current_span('Enviando o arquivo para o minIO')
def _senf_file_to_minio(filename):
    bucket_name = 'bucket'
    source_file = 'file.csv'
    destination_file = f'{filename}.csv'

    client.fput_object(
        bucket_name,
        destination_file,
        source_file,
    )


@app.task(bind=True)
def relatorio(self):
    logger.info('Criando relatório')
    with tracer.start_as_current_span('Fazendo a busca no banco'):
        with Session() as s:
            results = s.scalars(select(Task)).all()

            if results:
                _generate_csv(results)
                _senf_file_to_minio(self.request.id)

    logger.info('Relatório criado')

    return 'relatório!'
