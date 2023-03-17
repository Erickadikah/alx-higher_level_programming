"use strict";
//functions
function addTwo(num) {
    return num + 2;
}
function getUpper(val) {
    return val.toUpperCase();
}
function signUpUser(name, email, isPaid) {
}
let loginUser = (name, email, isPaid) => {
};
//UNION TYPES
// function getValue(myVal: number) {
//     if (myVal > 5) {
//         return true
//     }
//     return "200 OK"
// }
const getHello = (s) => {
    return "";
};
// const food = ["pizza", "burger", "hotdog", "tacos", "sushi"] // automatically ype string
const food = [1, 2, 3, 4, 5]; //automatically changes to number no annotation needed
food.map(food => {
    return `food is ${food}`;
});
function consoleError(errormsg) {
    console.log(errormsg);
}
function handleError(errormsg) {
    throw new Error(errormsg);
}
addTwo(5);
getUpper("Erick");
signUpUser("Erick", "Erickadikah@gamil.com", false);
loginUser("adikah", "a@gmail.com", true);
// console.log(signUpUser.email);
