#!/bin/bash
#Http all methodsserver accepts

curl -sI "$1" | grep -i 'allow' | cut -d " " -f2-
