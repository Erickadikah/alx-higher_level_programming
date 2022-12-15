#!/usr/bin/env bash
#display content using curl

curl -sI "$1" | grep -i 'content-length' | cut -d " " -f2
