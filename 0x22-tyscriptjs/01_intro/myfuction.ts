//functions

function addTwo(num: number) { //the value being added it si always going to be a number
    return num + 2
}

function getUpper(val: String) {
    return val.toUpperCase()
}

function signUpUser(name: string, email: string, isPaid: boolean){

}

let loginUser = (name: string, email: string, isPaid: boolean) => {

}


//UNION TYPES
// function getValue(myVal: number) {
//     if (myVal > 5) {
//         return true
//     }
//     return "200 OK"
// }

const getHello =(s: string): string => { //implementation in a arrow function
    return ""
}

const food = ["pizza", "burger", "hotdog", "tacos", "sushi"]

food.map(food => {
    return `food is ${food}`
})

addTwo(5)
getUpper("Erick")

signUpUser("Erick","Erickadikah@gamil.com",false)
loginUser("adikah", "a@gmail.com", true)
// console.log(signUpUser.email);