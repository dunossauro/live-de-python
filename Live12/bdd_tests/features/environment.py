import sys
from threading import Thread

from ipdb import post_mortem

from app.app import app
from bdd_tests.modules.thread_bottle import MyServer


def begin(server):
    app.run(server=server)


def before_all(context):
    sys.dont_write_bytecode = True
    context.base_url = 'http://127.0.0.1:8080'
    context.server = MyServer(host="localhost", port=8080)
    Thread(target=begin, args=(context.server,)).start()


def after_step(context, step):
    if step.status == 'failed':
        post_mortem(step.exc_traceback)


def after_all(context):
    context.server.shutdown()
