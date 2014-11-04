#!/usr/bin/python
# -*- coding: utf-8 -*-

# dependency.py file is part of slpkg.

# Copyright 2014 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# Utility for easy management packages in Slackware

# https://github.com/dslackw/slpkg

# Slpkg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys

from colors import GREY, ENDC

from greps import repo_requires

dep_results = []


def dependencies_pkg(name, repo):
    '''
    Build all dependencies of a package
    '''
    try:
        dependencies = []
        requires = repo_requires(name, repo)
        if requires:
            for req in requires:
                if req:
                    dependencies.append(req)
            if dependencies:
                dep_results.append(dependencies)
                for dep in dependencies:
                    sys.stdout.write("{0}.{1}".format(GREY, ENDC))
                    sys.stdout.flush()
                    dependencies_pkg(dep, repo)
        return dep_results
    except KeyboardInterrupt:
        print   # new line at exit
        sys.exit()
