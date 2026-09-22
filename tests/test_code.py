import importlib.util
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

# Load root code.py directly by path to avoid naming collision with Python stdlib 'code' module
ROOT_DIR = Path(__file__).resolve().parent.parent
CODE_FILE = ROOT_DIR / "code.py"

spec = importlib.util.spec_from_file_location("code_app", CODE_FILE)
code = importlib.util.module_from_spec(spec)
sys.modules["code_app"] = code
spec.loader.exec_module(code)


class TestCode(unittest.TestCase):
    def test_get_greeting(self):
        """Test that get_greeting returns the expected message."""
        self.assertEqual(code.get_greeting(), "Hello, World!")

    def test_main_output(self):
        """Test that main() prints the expected message to stdout."""
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            code.main()
            self.assertEqual(fake_stdout.getvalue().strip(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
