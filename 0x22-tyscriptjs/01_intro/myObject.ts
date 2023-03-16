// const User = {
//     name : "Erick",
//     email: "erickadika@gmail.com",
//     isActive: true,
// }

// // console.log(User);

// function createUser({name: string, isPaid: boolean}) {

// }

// let newUser = {name: "Erick", isPaid: false, email: "rick@rick.com"}

// createUser(newUser)

// function createCourse():{ name : string, price: number}{
//     return { name: "reactjs", price: 300}
// }

//Type aliases

    // type User = {
    //     name: string;
    //     email: string;
    //     isActive: boolean;

    // }

    // function createUser(user: User): User {
    //     return {name: "Erick", email: "", isActive: true}
    // }

    // createUser({name: "Erick", email: "", isActive: true})

    // export {}

//key words

type User = {
    readonly _id: string //readonly keyword
    name: string
    email: string
    isActive: boolean
    creditcardDetails?: number //optional key ?
}

let myUser: User = {
    _id: "1234",
    name: "Erick",
    email: "h@.com",
    isActive: true
}

myUser.email = "erick@.com"
// myUser._id = "12345" //error read only

type cardNumber ={
    cardnumber: String
}

type cardDate = {
    carddate: String
}

type cardDetails = cardNumber & cardDate  & { //intersection type use case, combine multiple types
    cvv: number
}//intersection type
