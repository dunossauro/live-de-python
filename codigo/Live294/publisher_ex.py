from redis import Redis

r = Redis()

r.publish('test', 'mensagem maluca!')
