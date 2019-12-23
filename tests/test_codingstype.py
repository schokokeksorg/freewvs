import unittest
import subprocess
import glob


class TestCodingstyle(unittest.TestCase):
    @staticmethod
    def test_codingstyle():
        pyfiles = ["freewvs", "update-freewvsdb",
                   "setup.py"] + glob.glob("tests/*.py")
        subprocess.run(["pycodestyle", "--ignore=W503"]
                       + pyfiles, check=True)
        subprocess.run(["pyflakes"] + pyfiles, check=True)

        pylint_disable = "missing-docstring,invalid-name," \
                         + "too-many-arguments,duplicate-code"
        subprocess.run(["pylint", "--disable=%s" % pylint_disable]
                       + pyfiles, check=True)


if __name__ == '__main__':
    unittest.main()
