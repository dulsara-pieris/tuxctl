#!/bin/bash
#Please use this file as base to all package files

echo "Download"
aria2c -x8 -s8 -d /tmp/tuxctl https://proof.ovh.net/files/1Mb.dat
#Please use higher values or lower depending on download size
