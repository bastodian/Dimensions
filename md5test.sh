#!/bin/bash

: <<'!'
    Script to compare md5sums contained in two files 
    (standard output of md5sum contains chksum first).

    Takes 2 files as input that contain the chksums
    and displays output in less.

    Make sure input files are in the correct order.

    md5test.sh md5file1 md5file2

    Author: Bastian Bentlage
    Email: bastian.bentlage@gmail.com
    License: Creative Commons Attribution
!

paste $1 $2 |\
    while read line
    do
        md5_1=`echo $line | awk '{ print $1 }'`
        md5_2=`echo $line | awk '{ print $3 }'`
        if [ "$md5_1" == "$md5_2" ]; then
            echo "OK! $md5_1 MATCHES $md5_2"
        else
            echo "MISMATCH! $md5_1 DOES NOT MATCH $md5_2"
        fi
    done |\
less
