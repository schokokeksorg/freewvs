import unittest
import subprocess
import glob


class TestCodingstyle(unittest.TestCase):
    def test_codingstyle(self):
        subprocess.run(["pycodestyle", "--ignore=W503", "freewvs"]
                       + glob.glob("tests/*.py"), check=True)
        subprocess.run(["pyflakes", "freewvs"]
                       + glob.glob("tests/*.py"), check=True)


if __name__ == '__main__':
    unittest.main()
