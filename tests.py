from unittest import TestCase
from unittest import mock

from mkpy224o import find_keys


class Mkpy224oTestCase(TestCase):
    def test_one(self):
        "Ensure it produces proper statistics"
        stats = []
        find_keys('foooo', 1, on_progress=lambda x: stats.append(x))
        self.assertGreater(len(stats), 0)
        self.assertIn('calc/sec', stats[0])
        self.assertIn('succ/sec', stats[0])
        self.assertIn('rest/sec', stats[0])
        self.assertIn('elapsed', stats[0])
        self.assertIn('estimate', stats[0])
        self.assertIn('remaining', stats[0])

    def test_one(self):
        "Ensure it produces proper keys"
        m = mock.Mock()
        keys = find_keys('foooo', 1, on_progress=m)
        self.assertEqual(len(keys), 1)
        self.assertIn('hostname', keys[0])
        self.assertIn('public', keys[0])
        self.assertIn('secret', keys[0])

    def test_ten(self):
        "Ensure the interval works"
        m = mock.Mock()
        keys = find_keys('foo', 10, on_progress=m)
        self.assertFalse(m.called)
        self.assertEqual(len(keys), 10)

    def test_one_hundred(self):
        "Ensure it produces correct number of keys"
        m = mock.Mock()
        keys = find_keys('foo', 100, on_progress=m, interval=1)
        self.assertTrue(m.called)
        self.assertEqual(len(keys), 100)
