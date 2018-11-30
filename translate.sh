#!/bin/bash
PATH=$PATH:/usr/local/bin
TRANS=`trans :en -b -no-autocorrect "$1"`

echo -n -e "$1\n$TRANS"
