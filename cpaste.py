#!/usr/bin/env python
import sys
import re
import traceback
import argparse
try:
    import requests
except ImportError:
    print("The 'requests' package is required.\nThis package can be installed with:\n\n\tpip install requests\n")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='?', help='File to Upload', metavar='filename.txt')
args = parser.parse_args()

if args.file:
    with open(args.file) as f:
        paste = f.read()
else:
    paste = sys.stdin.read()

paste_len = len(paste)
if paste_len > 4000000000 or paste_len < 5:
    print('Content length is too long/short: %s' % paste_len)
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
