#!/bin/bash

for file in ./pcap/*; do
    if [ -f "$file" ] && [ -x "$file" ]; then
        echo "Sending.. $file"
        /usr/bin/tcpreplay -i eth1 --mbps=20 $file
    fi
done
