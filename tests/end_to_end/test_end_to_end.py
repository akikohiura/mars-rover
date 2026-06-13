import subprocess
import sys
import unittest

class TestEndToEnd(unittest.TestCase):

    def test_user_can_process_multiple_rovers(self):
        user_input = (
            "5 5\n"
            "1 2 N\n"
            "LMLMLMLMM\n"
            "Y\n"
            "3 3 E\n"
            "MMRMMRMRRM\n"
            "N\n"
        )

        result = subprocess.run(
            [sys.executable, "src/main.py"],
            input=user_input,
            text=True,
            capture_output=True
        )

        self.assertEqual(0, result.returncode)
        self.assertIn("Rover 1 final position: 1 3 N", result.stdout)
        self.assertIn("Rover 2 final position: 5 1 E", result.stdout)


if __name__ == "__main__":
    unittest.main()