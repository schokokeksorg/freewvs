import unittest
import subprocess
import glob


class TestCodingstyle(unittest.TestCase):
    @staticmethod
    def test_codingstyle():
        pyfiles = ["freewvs", "update-freewvsdb", "setup.py"] + glob.glob("tests/*.py")
        subprocess.run(
            ["pycodestyle", "--ignore=W503,E501", "--max-line-length=88"] + pyfiles,
            check=True,
        )
        subprocess.run(["pyflakes"] + pyfiles, check=True)

        pylint_disable = (
            "missing-docstring,invalid-name,duplicate-code,"
            + "too-many-arguments,consider-using-with"
        )
        subprocess.run(["pylint", f"--disable={pylint_disable}"] + pyfiles, check=True)

        subprocess.run(["flake8", "--select=DUO"] + pyfiles, check=True)
        subprocess.run(["pyupgrade", "--py311-plus"] + pyfiles, check=True)


if __name__ == "__main__":
    unittest.main()
