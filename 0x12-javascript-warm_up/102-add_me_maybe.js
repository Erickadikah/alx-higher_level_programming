#!/usr/bin/node
exports.addMeMaybe = function (number, theFuction) {
  theFuction(++number);
};
