#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import threading
import time
import urllib3

import nut
import Server
from nut import Usb
from nut import Hook

def usbThread():
    Usb.daemon()

def nutThread():
    Server.run()

def run():
    urllib3.disable_warnings()

    print(r'                        ,;:;;,')
    print(r'                       ;;;;;')
    print(r'               .=\',    ;:;;:,')
    print(r'              /_\', "=. \';:;:;')
    print(r'              @=:__,  \,;:;:\'')
    print(r'                _(\.=  ;:;;\'')
    print(r'               `"_(  _/="`')
    print(r'                `"\'')

    nut.initTitles()
    nut.initFiles()
    nut.scan()

    Hook.init()

    threads = []
    threads.append(threading.Thread(target=usbThread, args=[]))
    threads.append(threading.Thread(target=nutThread, args=[]))

    for t in threads:
        t.daemon = True
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Exiting...')

if __name__ == '__main__':
    run()

Hook.call("exit")
