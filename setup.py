#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, shutil

from distutils.core import setup

setup(
    name='slpkg',
    py_modules=['slpkg'],
    version='1.0.1',
    description="Python tool to manage Slackware packages",
    keywords=["slpkg", "upgrade", "install", "remove", "view", "slackpkg", "tool"],
    author="dslackw",
    author_email="d.zlatanidis@gmail.com",
    url="https://github.com/dslackw/slpkg",
    download_url="https://github.com/dslackw/slpkg/archive/v1.0.1.tar.gz",
    scripts=['bin/slpkg'],
    package_data={"": ["LICENSE", "README.rst", "CHANGELOG"]},
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 0 - Alpha",
        "Topic :: Intersetup.pynet :: Utilities"],
    long_description=open("README.rst").read()
)

if 'install' in sys.argv:
    man_path = "/tmp/SBo/package-slpkg/usr/man/man8/"
    os.system("mkdir -p {}".format(man_path))
    if os.path.exists(man_path):
        print("Installing man pages")
        man_page = "man/slpkg.8"
        shutil.copy2(man_page, man_path)
        os.chmod(man_path + 'slpkg.8', int('444', 8))
