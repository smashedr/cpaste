#!/usr/bin/env bash

GET_PIP='https://bootstrap.pypa.io/get-pip.py'

which pip >/dev/null 2>&1
if [ "$?" != "0" ];then
    set -e
    temp=$(mktemp)
    curl -so ${temp} ${GET_PIP}
    sudo python ${temp}
    rm -f ${temp}
    set +e
fi

set -e
sudo pip -q install requests
sudo curl -so /usr/local/bin/cpaste https://git.cssnr.com/shane/cpaste/raw/master/cpaste.py
sudo chmod +x /usr/local/bin/cpaste
set +e

echo "Success - cpaste has been installed/updated."
