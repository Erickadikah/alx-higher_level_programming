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

    protected _courseCount = 1

    readonly city: string = "Bogota";
    constructor( 
        public email: string, 
        public password: string,
        // private userId: string
        ) {
    }

    private deleteToken() {
        console.log("delete token")
    }

    get getAppleEmail() : string{
        return `Apple ${this.email}`
    }

    get courseCount() : number {
        return this._courseCount
    }

    set courseCount(couserNum) {
        if (couserNum < 1) {
            throw new Error("Course number must be greater than 0")
        }
        this._courseCount = couserNum
    }
}

class SubUser extends User{
    isFamily: boolean = true
    changesCourseCount() {
        this._courseCount = 2
    }
} 

const Erick = new User ("erick2030@gamil.com", "Erick");
// Erick.deleteToken()