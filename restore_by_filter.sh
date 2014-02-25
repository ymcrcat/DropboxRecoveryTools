#!/bin/sh
filter=$1
grep $filter deleted_files.txt | while read -r line; do echo \"$line\"; done | xargs -L1 ./restore_file.py
