import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_output(self):
        with self.assertLogs(level="INFO") as log:
            main()
            self.assertIn("Hello, World!", log.output)

if __name__ == "__main__":
    unittest.main() 