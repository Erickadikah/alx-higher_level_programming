"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
let score = 33;
score = 44;
score = "44";
let Erick = { name: "Erick", id: 123456 };
Erick = { username: "Erick", id: 123456 };
getDBId(123456);
getDBId("ERICK");
function getDBId(id) {
    if (typeof id === "string") {
        id.toLowerCase();
    }
}
//array
const data = [1, 2, 3, 4,]; //error array designed for numbers only
const data2 = ["1", "2", "3", "4,"]; //error array designed for strings only
const data3 = ["1", "2", 3, 4,];
// export {}
let seatAllotment;
seatAllotment = "aisle";
