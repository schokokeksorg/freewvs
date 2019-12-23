#!/usr/bin/python3

import os
import glob
import pathlib
import shutil
import setuptools
import setuptools.command.install


class install_freewvsdb(setuptools.command.install.install):
    def run(self):
        dbpaths = ['/var/lib/freewvs/',
                   str(pathlib.Path.home()) + "/.cache/freewvs/"]

        target = False
        for dbpath in dbpaths:
            if not os.path.isdir(dbpath):
                try:
                    os.makedirs(dbpath)
                except PermissionError:
                    continue
            if os.access(dbpath, os.W_OK):
                target = dbpath
                break
        for j in glob.glob("freewvsdb/*.json"):
            shutil.copy(j, target)
        setuptools.command.install.install.run(self)


f = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'))
readme = f.read()
f.close()

setuptools.setup(
    name='freewvs',
    version="0.1.0",
    description="A free web vulnerability scanner",
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://freewvs.schokokeks.org/',
    packages=[],
    scripts=['freewvs', 'update-freewvsdb'],
    python_requires='>=3',
    license="CC0",
    keywords=['security', 'vulnerability', 'web'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    cmdclass={
        'install': install_freewvsdb
    }
)
