- [Requirements](#requirements)
- [Installation](#installation)
    - [Windows](#windows)
    - [Linux/Mac](#linuxmac)
- [Usage](#usage)

# cpaste

Python CLI Paste Bin API for http://p.cssnr.com/

https://git.cssnr.com/shane/php_pastebin

# Requirements

1. requests - http://docs.python-requests.org/en/master/user/install/#install

# Installation

## Windows

Download and move the executable to your %PATH% (example: `%SystemRoot%\system32`)
- http://cdn.cssnr.com/cpaste.exe

## Linux/Mac

### Automatic

Bash the `install.sh` script included with this repository, or:
- `bash <(curl -s https://git.cssnr.com/shane/cpaste/raw/master/install.sh)`

### Manual

1. `sudo pip install requests`
2. `sudo curl -so /usr/local/bin/cpaste https://git.cssnr.com/shane/cpaste/raw/master/cpaste.py`
3. `sudo chmod +x  /usr/local/bin/cpaste`

# Usage

#### From a PIPE

```
# rpm -qa | cpaste
http://p.cssnr.com/669
```

#### From a FILE

```
# cpaste cpaste.txt
http://p.cssnr.com/671
```

#### From STDIN

```
# cpaste
This is a test paste.
(Ctrl+D)
http://p.cssnr.com/670
```

# License

The MIT License (MIT)

Copyright (c) 2016 Shane

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
