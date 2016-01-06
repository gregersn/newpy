#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import os
import sys
import shutil

template_dir = './templates'


def copy_template(destination, template='basic.py'):
    home_dir = os.path.dirname(os.path.realpath(__file__))
    template = os.path.join(home_dir, template_dir, template)
    if not os.path.isfile(template):
        print("Template does not exist")
        print(template)
        return

    if os.path.isfile(destination):
        print("Destination exsists, will not overwrite")
        return

    if os.path.isdir(destination):
        print("Directory as destination, will use template file name")
        destination = os.path.join(destination, template)

    shutil.copyfile(template, destination)


def main():
    destination = os.path.join(os.getcwd(), sys.argv[1])
    copy_template(destination)

if __name__ == '__main__':
    main()
