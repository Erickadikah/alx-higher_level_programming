#!/bin/bash
#script that sends DELETE request

curl -X "$1" DELETE "$1" -s
