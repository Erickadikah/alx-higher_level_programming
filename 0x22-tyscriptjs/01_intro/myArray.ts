const superHeros: string[] = [] //empty array
const superPower: Array<number> = [] 

type User = {
    name: string
    isActive: boolean
}

const allUsers: User[] = []


superHeros.push("spiderman", "batman", "superman")
superPower.push(100, 200, 300)

console.log(superHeros, superPower)

allUsers.push({name: "Erick", isActive: true})

export {}