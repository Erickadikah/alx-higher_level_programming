#!/bin/bash
# script that takes url 
#displays the body of response
curl "$1" | wc -c
