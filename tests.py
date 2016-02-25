import unittest
import json
from movie import OpenMDB

class TestOpenMDB(unittest.TestCase):
    def setUp(self):
        self.m = OpenMDB()

    def test_build_url(self):
        params = {'plot': 'full', 'i': '1234'}
        url = self.m._build_omdbapi_url(params)
        real_url = 'http://www.omdbapi.com/?i=1234&plot=full&apikey=yy5at44a4hzqqbsgnm4u47ju'
        self.assertEqual(url, real_url)

    def test_query_w_existing_movie(self):
        params = {'t': 'shawshank', 'plot': 'full', 'tomatoes': True}
        r = self.m.query(params)
        self.assertEqual('1994', r['Year'])

    def test_query_w_non_existing_movie(self):
        params = {'t': 'shawnshank crap xx', 'plot': 'full', 'tomatoes': True}
        r = self.m.query(params)
        msg = "Movie not found!"
        self.assertEqual(msg, r['Error'])

if __name__ == '__main__':
    unittest.main()