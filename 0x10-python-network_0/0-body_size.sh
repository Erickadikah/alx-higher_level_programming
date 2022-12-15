#!/bin/bash
# script that takes url and displays the body of response
curl "$1" | wc -c
