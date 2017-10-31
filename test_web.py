import os
import flask
import unittest

from run import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """inital test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """inital test. ensure that the database exists"""
        tester = os.path.exists("db/db.sql")
        self.assertTrue(tester)

if __name__ == '__main__':
    unittest.main()
