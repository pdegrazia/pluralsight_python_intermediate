import unittest
from reader import Reader


class ReaderTest(unittest.TestCase):
    def setUp(self):
        self.r = Reader('text.txt')

    def tearDown(self):
        self.r.close()

    def test_read(self):
        text = self.r.read()
        assert text == 'some test text'

    def test_filename(self):
        assert self.r.filename == 'text.txt'