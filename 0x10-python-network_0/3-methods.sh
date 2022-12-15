#!/bin/bash
#Http all methods server accepts
curl -sI "$1" | grep -i 'allow' | cut -d " " -f2-
