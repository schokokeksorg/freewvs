import unittest
import glob
import json
import sys
import difflib
import re


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
            if orig != new:
                print("json %s not valid" % f)
                sys.stdout.writelines(difflib.unified_diff(orig, new))
                valid = False
        self.assertTrue(valid)

    def test_json_values(self):
        jconfig = []
        for cfile in glob.glob('freewvsdb/*.json'):
            with open(cfile) as json_file:
                jconfig += json.load(json_file)

        mkeys = set(['name', 'url', 'safe', 'vuln', 'detection'])
        for item in jconfig:

            # check for all mandatory keys
            self.assertEqual(mkeys.intersection(item.keys()), mkeys,
                             msg="Missing key in %s" % item['name'])

            # check we have at least one detection
            self.assertTrue(len(item['detection']) >= 1,
                            msg="No detection in %s" % item['name'])

            # vuln needs to be CVE or HTTPS URL
            self.assertTrue(re.match("^CVE-[0-9]*-[0-9]*$", item['vuln'])
                            or item['vuln'].startswith("https://"),
                            msg="%s: Invalid vuln %s" %
                            (item['name'], item['vuln']))
            for det in item['detection']:
                self.assertTrue(type(det['subdir']) == int,
                                msg="%s: subdir not int" % item['name'])


if __name__ == '__main__':
    unittest.main()
