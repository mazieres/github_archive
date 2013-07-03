#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import datetime

# Example: /home/mazieres/archive/github/
ARCHIVE_FOLDER = ""

base_url = "http://data.githubarchive.org/"

base = datetime.datetime(year=2011,month=2,day=12)
now = datetime.datetime.utcnow()
delta = (now - base)

dateList = [ now - datetime.timedelta(days=x) for x in range(0,delta.days + 1) ]

for d in reversed(dateList):
    date = '-'.join([str("%02d" % x) for x in d.timetuple()[:3]])
    for h in range(24):
        hour = date + '-' + str(h)
        url = base_url + hour + '.json.gz'
        dest_file = ARCHIVE_FOLDER + 'github_archive_' + hour + '.json.gz'
        if not os.path.exists(dest_file):
            r = requests.get(url)
            if 'json' in r.headers['content-type']:
                f = open(dest_file, "wb")
                f.write(r.content)
                f.close()