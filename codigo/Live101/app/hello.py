from flask import Blueprint
from time import sleep

bp_hello = Blueprint('Hello', __name__)


@bp_hello.route('/ping')
def ping():
    return 'pong'


@bp_hello.route('/wait')
def wait():
    sleep(3)
    return 'waitado'
