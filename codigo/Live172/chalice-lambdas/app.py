from chalice import Chalice, Rate
import logging


app = Chalice(app_name='chalice-lambdas')
app.log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return {'message': 'Olar Chalice!'}


@app.route('/batatinhas')
def batatinhas():
    return {'message': 'Olar batatinhas!'}


@app.route('/query')
def query():
    return {
        'message': 'Olar Query!',
        'params': app.current_request.query_params
    }


@app.route('/meu-post', methods=['POST'])
def post_func():
    return {
        'message': 'Olar Query!',
        'params': app.current_request.json_body
    }


@app.lambda_function(name='batata-function')
def my_lambda(request, context):
    return {}


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduler(event):
    app.log.info('Executei o scheeeeedddddddd!!!!')


@app.on_s3_event(bucket='live-de-bucket')
def s3_event(event):
    app.log.info(f'{event.bucket}, {event.key}')
