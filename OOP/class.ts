type Role = "Admin" | "Member" | "Regular";

class User {
    name: string;
    role: Role;
    
    constructor(name: string, role: Role){
        this.name = name
        this.role = role
    }

    message() {
        const message = `${this.name} created as ${this.role}`
        return message
    }
}

const Andrew = new User("Andrew", "Admin")
console.log(Andrew.message())