#!/usr/bin/python
# -*- coding: utf-8 -*-

# repoenable.py file is part of slpkg.

# Copyright 2014-2015 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# Slpkg is a user-friendly package manager for Slackware installations

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


import os

from slpkg.utils import Utils
from slpkg.dialog_box import DialogUtil
from slpkg.__metadata__ import MetaData as _meta_


class RepoEnable(object):
    """Read repositories.conf file and update with new enabled or
    disabled repositories
    """
    def __init__(self):
        self.meta = _meta_
        self.tag = "[REPOSITORIES]"
        self.tag_line = False
        self.repositories_conf = "repositories.conf"
        self.conf = Utils().read_file(
            self.meta.conf_path + self.repositories_conf)
        self.enabled = []
        self.disabled = []
        self.selected = []

    def choose(self):
        """Choose repositories
        """
        keys = """
Keys: SPACE   select or deselect the highlighted repositories,
             move it between the left and right lists
          ^       move the focus to the left list
          $       move the focus to the right list
        TAB     move focus
      ENTER   press the focused button

      Disabled  <-------- REPOSITORIES ------->  Enabled"""
        self.read_enabled()
        self.read_disabled()
        self.selected = DialogUtil(self.disabled, text=keys,
                                   title="Enable | Disable  Repositories",
                                   backtitle="",
                                   status=False).buildlist(self.enabled)
        self.update_repos()
        self.clear_screen()
        self.reference()

    def read_enabled(self):
        """Read enable repositories
        """
        for line in self.conf.splitlines():
            line = line.lstrip()
            if self.tag in line:
                self.tag_line = True
            if (line and self.tag_line and not line.startswith("#") and
                    self.tag not in line):
                self.enabled.append(line)
        self.tag_line = False

    def read_disabled(self):
        """Read disable repositories
        """
        for line in self.conf.splitlines():
            line = line.lstrip()
            if self.tag in line:
                self.tag_line = True
            if self.tag_line and line.startswith("#"):
                line = "".join(line.split("#")).strip()
                self.disabled.append(line)
        self.tag_line = False

    def update_repos(self):
        """Update repositories.conf file with enabled or disabled
        repositories
        """
        with open("{0}{1}".format(self.meta.conf_path,
                                  self.repositories_conf), "w") as new_conf:
            for line in self.conf.splitlines():
                line = line.lstrip()
                if self.tag in line:
                    self.tag_line = True
                if self.tag_line and line.startswith("#"):
                    repo = "".join(line.split("#")).strip()
                    if repo in self.selected:
                        new_conf.write(line.replace(line, repo + "\n"))
                        continue
                if (self.tag_line and not line.startswith("#") and
                        line != self.tag):
                    repo = line.strip()
                    if repo not in self.selected:
                        new_conf.write(line.replace(line, "# " + line + "\n"))
                        continue
                new_conf.write(line + "\n")

    def clear_screen(self):
        """Clear screen
        """
        os.system("clear")

    def reference(self):
        """Reference enable repositories
        """
        print("Enabled repositories: {0}".format(", ".join(self.selected)))