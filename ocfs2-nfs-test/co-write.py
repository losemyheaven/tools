#! /usr/bin/env python3

import sys
import os
from pathlib import Path


def file_size(f):
    statinfo = os.stat(f)
    print("file size", statinfo.st_size)
    return statinfo.st_size


def file_exists(f):
    my_file = Path(f)
    if my_file.is_file():
        return True
    return False

def cycle_write(f, loops, step):
    content = "l"*1024
    size = file_size(f)

    with open(f, "r+") as ff:
        offset = 0
        for i in range(0, loops):
            if offset + len(content) >= size:
                offset = 0
            ff.seek(offset)
            ff.write(content)
            offset += step

def cycle_read(f, loops, size):

    with open(f, "r+") as ff:
        for i in range(0, loops):
            ret = ff.read(size)
            if ret == 0:
                return


def main():
    fs = sys.argv[1]
    loops = int(sys.argv[2])
    assert(sys.argv[1] in ["ocfs2", "nfs"])
    f = "/mnt/" + fs + "/f1"
    assert(file_exists(f))
    #cycle_write(f, loops, 4<<10)
    cycle_read(f, loops, 4<<10)

import time
time.sleep(3)
print("start in 1 sec")
time.sleep(1)

main()
