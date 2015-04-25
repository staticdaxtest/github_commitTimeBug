#!/usr/bin/env python

import subprocess
import random

date_list = ['04/26/15','04/27/15','04/28/15']


for item in date_list:
    # script = 'hwclock --set --date="'+item+' 00:00";hwclock --hctosys;echo "$RANDOM" > /root/github_commitTimeBug/$RANDOM;~/github_commitTimeBug/auto.sh;'
    script = 'hwclock --set --date="'+item+' 00:00";hwclock --hctosys;'
    print subprocess.check_output(script,shell=True)
    f = open('/root/github_commitTimeBug/'+str(random.random()),'a')
    f.write(str(random.random()))
    f.close()
    subprocess.check_output('/root/github_commitTimeBug/auto.sh')
