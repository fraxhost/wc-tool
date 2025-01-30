import unittest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.ccwc_fraxhost.utils import get_total_characters_from_content


class TestUtils(unittest.TestCase):

    def test_get_total_bytes_from_content(self):
        # arrange
        content = 'Hello World!'
        # act
        result = get_total_characters_from_content(content)
        # assert
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()