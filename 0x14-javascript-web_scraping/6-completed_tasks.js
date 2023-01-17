#!/usr/bin/node

const fs = require ('fs')
const request = require('request')
const API_URL = process.argv[2];

request.get(API_URL,
		function(error, respons, body)
