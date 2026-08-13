// Encapsulation(Data Hiding & Bundling)
// This is hthe parctice of bundling data abd method that operate that data into a single unit(the class)
// we enforce encapsulation using Access modifiers(public, private, protected)

type AccountType = "Organization" | "regular" | "Project Zero";
type Status = 0 | 200 | 201 | 300 | 400 | 401 | 500;

// my own hash function
const hashPassword = (text_password: string) => {
    let hash: number = 5381

    for (let i=0; i < text_password.length; i++){
        const charCode = text_password.charCodeAt(i);
        console.log(charCode); // checking

        hash = ((hash << 5) + hash) + charCode
        hash = hash & hash
    }

    return (hash >>> 0).toString(16)
}

class Account{

    public user_name: string;
    public user_profile_pic: string;
    protected account_type: AccountType;
    private api_key: string;
    private password: string;

    constructor (
        user_name: string,
        user_profile_pic:string,
        account_type: AccountType,
        api_key: string,
        password: string
    ){
        this.user_name = user_name;
        this.user_profile_pic = user_profile_pic;
        this.account_type = account_type;
        this.api_key = api_key;
        this.password = hashPassword(password);
    }

    public account_creation_message(){
        return {
            status: 201 as Status,
            message: `Congratulations ${this.user_name} account created`,
            ok: true,
            data : {
                user_name: this.user_name,
                user_profile_pic : this.user_profile_pic,
            }
        }
    }

    public login(user_name: string, password: string){
        try {
            password = hashPassword(password)
            if (password == this.password && user_name == this.user_name){
                return {
                    status: 200 as Status,
                    ok: true,
                    message: `User ${this.user_name} login successful`,
                    data: {
                        user_name: this.user_name,
                        user_profile_pic : this.user_profile_pic,
                    }
                }
            }
            else {
                return {
                    status: 500 as Status,
                    ok: true,
                    message: `Check your user name and password`
                }
            }
        }
        catch(err){
            console.log({
                    err: err,
                    status: 500 as Status,
                    ok: false,
                    message: "Internal Server Error"
                })
        }



    }
}


class OrganiztionAccount extends Account{
    public team_size: number;
    public organization_domain: string;
    public net_worth_2030: string;

    constructor(
        user_name: string,
        user_profile_pic:string,
        account_type: AccountType,
        api_key: string,
        password: string,
        team_size: number,
        organization_domain: string,
        net_worth_2030: string,
    ){
        
    }
}