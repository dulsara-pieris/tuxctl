#!/bin/bash
#Please use this file as base to all package files

echo "Download"
aria2c -x8 -s8 -d /tmp/tuxctl https://ipv4.download.thinkbroadband.com/5MB.zip
#Please use higher values or lower depending on download size
