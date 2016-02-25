import urllib
import urlparse
import json
import redis

import requests


API_KEY = "yy5at44a4hzqqbsgnm4u47ju"

BASE_URL = "http://www.omdbapi.com/?"


class OpenMDB:
    def __init__(self):
        self.session = requests.session() 

    def query(self, kwargs):
        # comment
        # error handling
        url = self._build_omdbapi_url(kwargs)
        r = self.session.get(url)

        return json.loads(r.content)

    def _build_omdbapi_url(self, kwargs):
        kwargs.update({'apikey': API_KEY})
        qs = urllib.urlencode(kwargs)

        return "%s%s" %(BASE_URL, qs)


if __name__ == '__main__':
    rd = redis.Redis()
    m = OpenMDB()

    while True:
        n = rd.llen('movie_q')

        if n > 0:
            print "\n\n-------"
            print '%d in queue' % n  
            params = rd.rpop('movie_q')
            print 'get request %s' % params
            params = json.loads(params)
            if params:
                print 'fetching movie ...'
                mov = m.query(params)
                if mov.get('Response', '') != 'False':
                    rd.lpush('movie_results', mov)
                    print 'publish to movie_results; Done ...'
                else:
                    print 'bad results'
                print mov
                print "-------\n\n"
