"use strict";
// class User {
//     private email: string;
//     private password: string;
//     private city: string = "Bogota";
//     constructor(email: string, password: string) {
//         this.email = email;
//         this.password = password;
//     }
// }
// const Erick = new User ("erick2030@gamil.com", "Erick");
// // Erick.city
class User {
    constructor(email, password) {
        this.email = email;
        this.password = password;
        this._courseCount = 1;
        this.city = "Bogota";
    }
    deleteToken() {
        console.log("delete token");
    }
    get getAppleEmail() {
        return `Apple ${this.email}`;
    }
    get courseCount() {
        return this._courseCount;
    }
    set courseCount(couserNum) {
        if (couserNum < 1) {
            throw new Error("Course number must be greater than 0");
        }
        this._courseCount = couserNum;
    }
}
class SubUser extends User {
    constructor() {
        super(...arguments);
        this.isFamily = true;
    }
    changesCourseCount() {
        this._courseCount = 2;
    }
}
const Erick = new User("erick2030@gamil.com", "Erick");
// Erick.deleteToken()
