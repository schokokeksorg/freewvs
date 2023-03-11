import unittest
import glob
import json
import sys
import difflib
import re


def versioncompare(safe_version, find_version):
    safe_version_tup = [int(x) for x in safe_version.split(".")]
    find_version_tup = [int(x) for x in find_version.split(".")]
    return find_version_tup < safe_version_tup


class TestJsonLint(unittest.TestCase):
    @unittest.skipIf(
        sys.version_info < (3, 6, 0), "json.dumps force-sorts on python 3.5"
    )
    def test_json_lint(self):
        valid = True
        for f in glob.glob("freewvsdb/*.json"):
            fp = open(f, encoding="ascii")
            orig = fp.read()
            fp.close()
            tmp = json.loads(orig)
            new = json.dumps(tmp, indent=2) + "\n"
            if orig != new:
                print(f"json {f} not valid")
                sys.stdout.writelines(difflib.unified_diff(orig, new))
                valid = False
        self.assertTrue(valid)

    def test_json_values(self):
        jconfig = []
        for cfile in glob.glob("freewvsdb/*.json"):
            with open(cfile, encoding="ascii") as json_file:
                jconfig += json.load(json_file)

        mkeys = {"name", "url", "safe", "vuln", "detection"}
        for item in jconfig:
            # check for all mandatory keys
            self.assertEqual(
                mkeys.intersection(item.keys()),
                mkeys,
                msg=f"Missing key in {item['name']}",
            )

            # check we have at least one detection
            self.assertTrue(
                len(item["detection"]) >= 1, msg=f"No detection in {item['name']}"
            )

            # vuln needs to be CVE or HTTPS URL
            self.assertTrue(
                re.match("^CVE-[0-9]*-[0-9]*$", item["vuln"])
                or item["vuln"].startswith("https://"),
                msg=f"{item['name']}: Invalid vuln {item['vuln']}",
            )

            # make sure safe is a version
            if item["safe"] != "":
                # we have a theoretical reDoS here, but
                # this is no external data, therefore ok
                self.assertTrue(
                    re.match(r'^([0-9]+\.)*[0-9]+$', item["safe"]),  # noqa: DUO138
                    msg=f"{item['name']}: Invalid safe version {item['safe']}",
                )

            # make sure old_safe is properly sorted
            if "old_safe" in item:
                old_safe = item["old_safe"].split(",")
                for i in range(1, len(old_safe)):
                    self.assertTrue(
                        versioncompare(old_safe[i - 1], old_safe[i]),
                        msg=f"{item['name']}: Invalid old_safe"
                        " ordering {item['old_safe']}",
                    )

            # make sure latest is not outdated
            if "latest" in item and item["safe"] != "":
                self.assertTrue(
                    not versioncompare(item["safe"], item["latest"]),
                    msg=f"{item['name']}: Safe version "
                    "{item['safe']} newer than latest"
                    " {item['latest']}",
                )

            # subdir needs to be integer
            for det in item["detection"]:
                self.assertTrue(
                    isinstance(det["subdir"], int),
                    msg=f"{item['name']}: subdir not int",
                )


if __name__ == "__main__":
    unittest.main()
