let score: number | string = 33;

score = 44

score = "44"

type  User = { 
    name:  string ;
    id: number;
}

type  Admin = {
    username:  string ;
    id: number;
}

let Erick: User | Admin = { name: "Erick", id: 123456 }


Erick = {username: "Erick", id: 123456}

getDBId(123456)
getDBId("ERICK")


function getDBId(id: number | string) {
    if (typeof id === "string") {
        id.toLowerCase()
    } 
}


//array

const data: number[] = [1, 2, 3, 4,] //error array designed for numbers only
const data2: string[] = ["1", "2", "3", "4,"] //error array designed for strings only
const data3: (number| string)[] = ["1", "2", 3, 4,]
// export {}

let seatAllotment: "aisle" | "middle"  | "window"

seatAllotment = "aisle"
// seatAllotment = "crew" not allowed

export {}