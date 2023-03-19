"use strict";
const score = [];
const names = [];
function identityOne(val) {
    return val;
}
function identityTwo(val) {
    return val;
}
function identityThree(val) {
    return val;
}
// identityThree("5")
// console.log(identityThree(5))
function identityFour(val) {
    return val;
}
// identityFour<Bottle>({brand: "Coca Cola", type: 1})
function getSearchProducts(products) {
    // some database operation logic
    const myIndex = 3;
    return products[3];
}
const getMoreSearchProducts = (products) => {
    //do some database operations
    const myIndex = 4;
    return products[myIndex];
}; //generic arrow function
function anotherFunction(valueOne, valueTwo) {
    return {
        valueOne,
        valueTwo
    };
}
class Sellable {
    constructor() {
        this.cart = [];
    }
    addToCart(product) {
        this.cart.push(product);
    }
}
