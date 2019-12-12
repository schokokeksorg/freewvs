import unittest
import glob
import json
import sys
import difflib


class TestJsonLint(unittest.TestCase):

    @unittest.skipIf(sys.version_info < (3, 6, 0),
                     "json.dumps force-sorts on python 3.5")
    def test_json_lint(self):
        valid = True
        for f in glob.glob("freewvsdb/*.json"):
            fp = open(f, "r")
            orig = fp.read()
            fp.close()
            tmp = json.loads(orig)
            new = json.dumps(tmp, indent=2)
            if (orig != new):
                print("json %s not valid" % f)
                sys.stdout.writelines(difflib.unified_diff(orig, new))
                valid = False
        if not valid:
            raise Exception("Unlinted json files found")


if __name__ == '__main__':
    unittest.main()
