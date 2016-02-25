import urlparse
from bottle import route, run, get, post, request 
import redis
import json

from movie import OpenMDB

TASK_Q = 'movie_q'
RESULTS_Q = 'movie_results'

rd = redis.Redis()

@post('/query')
def query():
    # comment 
    # error handling
    m = OpenMDB()
    params = request.json
    msg = json.dumps(params)
    rd.lpush(TASK_Q, msg)

    return {'status': 'ok'}

@get('/status')
def status():
    n = rd.llen(RESULTS_Q)
    msg = '%d movies in queue, do sth!' % n
    return {'status': msg}

run(host='localhost', port=8080)


# comment 
# error handling
# complete test
# rabbitMQ instead of redis 
# search movie
# more params 