#!usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const map1 = list.map(x => x * 2);
console.log(map1);
