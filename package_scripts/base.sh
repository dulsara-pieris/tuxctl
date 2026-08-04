#!/bin/bash
#Please use this file as base to all package files

echo "Download"
aria2c -x8 -s8 -d /tmp/tuxctl https://geo.mirror.pkgbuild.com/core/os/x86_64/bash-5.3.3-1-x86_64.pkg.tar.zst
#Please use higher values or lower depending on download size
