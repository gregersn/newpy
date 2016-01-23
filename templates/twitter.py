#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import json
import twitter

def loadkeys(filename):
    with open(filename, 'rb') as f:
        apiconifg = json.load(f)

    return apiconfig

def initapi(keys):
    api = twitter.Api(consumer_key=keys['consumer_key'],
                      consumer_secret=keys['consumer_secret'],
                      access_token_key=keys['access_token_key'],
                      access_token_secret=keys['access_token_secret'])

    return api


def main():
    pass

if __name__ == '__main__':
    main()
