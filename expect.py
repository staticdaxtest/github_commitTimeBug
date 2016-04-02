#!/usr/bin/env python

import sys
import pexpect
expect_list = ["Password for 'https://staticdax@github.com':"]
password = 't0D4y!1@DE#bsf'

p = pexpect.spawn('git push origin master')
try:
    idx = p.expect(expect_list)
    print p.before + expect_list[idx],
    if idx == 0:
        print "sending pass"
        p.sendline(password)
except pexpect.TIMEOUT:
    print >>sys.stderr, 'timeout'
except pexpect.EOF:
    print p.before
    print >>sys.stderr, '<end>'
