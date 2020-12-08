#!/bin/bash

set -eo pipefail

DAY="1"

cd /`printf %d-2 $DAY`/
python3 -m compileall >/dev/null

if [ -f `printf %d-2 $DAY` ] ; then
    time sh -c ./`printf %d-1 $DAY`/; ./`printf %d-2.py $DAY`
else
    echo "not sure how to run this"
    exit 1
fi
