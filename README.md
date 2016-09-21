# cpaste

Python CLI Paste Bin API for http://p.cssnr.com/

https://git.cssnr.com/shane/php_pastebin

# Requirements

1. requests - http://docs.python-requests.org/en/master/user/install/#install

# Installation

1. `sudo pip install requests`
2. `sudo curl -so /usr/local/bin/cpaste https://git.cssnr.com/shane/cpaste/raw/master/cpaste.py`
3. `sudo chmod +x  /usr/local/bin/cpaste`

# Usage

- From a PIPE:

```
# rpm -qa | cpaste
http://p.cssnr.com/669
```

- From a FILE:

```
# cpaste /usr/local/bin/cpaste
http://p.cssnr.com/671
```

- From STDIN:

```
# cpaste
This is a test paste.
(Ctrl+D)
http://p.cssnr.com/670
```
