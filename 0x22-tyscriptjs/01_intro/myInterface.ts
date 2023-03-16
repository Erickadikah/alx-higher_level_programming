import { GitHub } from "@mui/icons-material";

interface User { //more powerfull than type more unique
    readonly dbId: number;
    email: string;
    userId: number;
    googleId?: string;
    // startTrial: () => string;
    startTrial(): string;
    getCoupon(couponname: string, value: number): number;
}

interface User {
    GithubToken: string;
}
//INterface can be extended TO Inheritance
interface Admin extends User {
    role: "admin" | "ta" | "student";
}

const Erick: Admin = {
    dbId: 12345,
    GithubToken: "github",
    email: 'rick@gamil',
    userId: 19990,
    startTrial: () => {
        return 'trial started'
},
    getCoupon: (name: "erick2030", off: 10) => {
        return 10;
    }
}

Erick.email = "rick@gmail";


export {}