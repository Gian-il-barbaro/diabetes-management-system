import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'test', 'python'))

if __name__ == '__main__':
    loader = unittest.TestLoader()
    test_dir = os.path.join(os.path.dirname(__file__), 'src', 'test', 'python')
    suite = loader.discover(test_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    sys.exit(0 if result.wasSuccessful() else 1)