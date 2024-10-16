import unittest
from scanner.sql_injection import check_sql_injection
from scanner.xss import check_xss

class TestScanner(unittest.TestCase):
    def test_sql_injection(self):
        self.assertTrue(check_sql_injection('http://test.com'))
    
    def test_xss(self):
        self.assertTrue(check_xss('http://test.com'))

if __name__ == '__main__':
    unittest.main()
