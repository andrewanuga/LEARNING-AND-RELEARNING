const sum = (a: number, b: number) => {
    try{
        if(typeof a !== "number" || typeof b !== "number") {
        throw new Error("Both arguments must be numbers");
    }
    return a + b;
    }
    catch(error) {
        console.log(`error: ${error}`)
}
}
console.log(sum(1,3))
console.log(sum(2,3))

// I want my code to crash and throw an error when I pass in a string
console.log(sum(6,3))