import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world yeah'
        self.assertEqual(s.split(), ['hello', 'world', 'yeah'])
        with self.assertRaises(TypeError):
            s.split(2)

    @unittest.skip("demonstrating skipping")
    def test_skipped_unittest(self):
        self.assertEqual(True, True)
