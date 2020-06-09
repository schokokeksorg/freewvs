import unittest
import subprocess
import glob
import os
import tempfile
import shutil
import re
import difflib

TESTDATA_REPO = "https://github.com/schokokeksorg/freewvs-testdata"


class TestFreewvsData(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("RUN_ONLINETESTS"),
                         "Not running online tests")
    def test_freewvs_testdata(self):
        tmp = tempfile.mkdtemp(prefix="testdata")
        if os.environ.get("TESTDATA_REPOSITORY"):
            os.symlink(os.environ.get("TESTDATA_REPOSITORY"),
                       tmp + "/testdata")
        else:
            subprocess.run(["git", "clone", "--depth=1",
                            TESTDATA_REPO,
                            tmp + "/testdata"],
                           check=True)

        #for tdir in glob.glob(tmp + "/testdata/webapps/*"):
        if 0:
            bdir = os.path.basename(tdir)
            for tarball in glob.glob(tdir + "/dist/*"):
                shutil.unpack_archive(tarball, "%s/%s/%s-src"
                                      % (tmp, bdir, os.path.basename(tarball)))
            fwrun = subprocess.run(["./freewvs", "-a", tmp + "/" + bdir],
                                   stdout=subprocess.PIPE, check=True)
            fwdata = re.sub(tmp, "[dir]", fwrun.stdout.decode("utf-8"))
            fwclean = re.sub(r' \(.* ', " ", fwdata)
            f = open(tdir + "/refdata-a.txt")
            refdata = f.read()
            f.close()
            refclean = re.sub(r' \(.* ', " ", refdata)
            fwclean = sorted(fwclean.split("\n"))
            refclean = sorted(refclean.split("\n"))
            if refclean != fwclean:
                print("\n".join(difflib.ndiff(refclean, fwclean)))
            self.assertEqual(refclean, fwclean,
                             msg="Output in %s does not match" % bdir)

        # misc tests, for read errors, garbage data etc.
        subprocess.run(["./freewvs", "-a", tmp + "/testdata/misc/"],
                       stdout=subprocess.PIPE, check=True)


if __name__ == '__main__':
    unittest.main()
