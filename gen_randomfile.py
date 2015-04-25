#!/usr/bin/env python

import subprocess

date_list = ['04/26/15','04/27/15','04/28/15']


for item in date_list:
    script = 'hwclock --set --date="'+item+' 00:00";hwclock --hctosys;echo "$RANDOM" > /staticdax/github_commitTimeBug/$RANDOM;~/github_commitTimeBug/auto.sh;'
    subprocess.check_output(script,shell=True)
