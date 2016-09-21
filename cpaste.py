#!/usr/bin/env python
import sys
import re
import traceback
import requests

try:
    file = sys.argv[1]
    try:
        with open(file) as f:
            paste = f.read()
    except:
        print(traceback.format_exc())
        sys.exit(1)
except IndexError:
    paste = sys.stdin.read()

if len(paste) > 4000000000 or len(paste) < 5:
    print('Content length is too long/short: %s' % len(paste))
    sys.exit(1)

try:
    data = {'paste': paste}
    uri = 'http://p.cssnr.com/paste.php'
    request = requests.post(uri, data=data, timeout=10)
    pattern = 'https?:\/\/[a-zA-Z0-9\-\.\/]+\/[0-9]+'
    match = re.search(pattern, request.text)
    response = match.group(0)
    print(response)
except:
    print('Error creating paste:\n%s' % traceback.format_exc())
    sys.exit(1)

