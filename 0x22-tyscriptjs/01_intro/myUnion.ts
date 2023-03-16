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

export {}