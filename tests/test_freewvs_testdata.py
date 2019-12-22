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
    @unittest.skipUnless(os.environ.get("FREEWVS_ONLINETESTS"),
                         "Not running online tests")
    def test_freewvs_testdata(self):
        tmp = tempfile.mkdtemp(prefix="freewvs-testdata")
        if os.environ.get("FREEWVS_TESTDATA_REPOSITORY"):
            os.symlink(os.environ.get("FREEWVS_TESTDATA_REPOSITORY"),
                       tmp + "/freewvs-testdata")
        else:
            subprocess.run(["git", "clone", "--depth=1",
                            TESTDATA_REPO,
                            tmp + "/freewvs-testdata"],
                           check=True)

        for tdir in glob.glob(tmp + "/freewvs-testdata/webapps/*"):
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


if __name__ == '__main__':
    unittest.main()
