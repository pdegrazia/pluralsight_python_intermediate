import unittest
from reader import Reader


class ReaderTest(unittest.TestCase):
    def setUp(self):
        self.r = Reader('text.txt')

    def tearDown(self):
        self.r.close()

    def test_read(self):
        actual_text = self.r.read()
        assert actual_text == 'some test text'

    def test_filename(self):
        assert self.r.filename == 'text.txt'

    def test_bzipped(self):
        r = Reader('../compressed/test.bz2')
        actual_text = r.read()
        assert actual_text == 'datacompressedwithbzip'
        r.close()