#!/usr/bin/node
const count = process.argv.lenth;
console.log(count === 2 ? 'No argment' : count === 3 ? 'Argument found' : 'Arguments found');

