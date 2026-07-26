#include <stdio.h>
#include <stdbool.h> // Required for 'bool, 'true  and false' meaning Standard Boolean Library

int main(){
    const int score = 100;
    if (score >= 100){
        printf("%s","level Completed");
    }
    else {
        printf("%s", "Game Over");
    }
    return 0;
}

void ageChecker(){ // If function is defined wwith void that means it does not output a return statement
    int age;
    bool access = false;
    scanf("%d", &age);

    if(age < 18){
        printf("%s","Sorry you are too young\n");
    }
    else if(age >= 18){
        printf("%s","Age verified\n");
        access = true;
        printf("%s","Access Granted\n");
    }
    else{
        printf("%s", "Enter a valid Age\n");
    }
    return; // u can use `return` to exit early in a void function
}


// using switch

void ageCheckerSwitch(){
    int age;
    bool access = false;
    printf("%s","Enter your Age: ");
    scanf("%d", &age);

    if (age < 18){ //switch can not compare like age > 18
        printf("%s", "Too Young\n");
    }
    else if (age >= 18){
        printf("%s","Old Enough\n");
        access = true;
        switch(access){
            case true:
                printf("%s", "Access Granted\n");
                break;
            case false:
                printf("%s", "Opps An Error Occured\n");
                break;
            default:
                printf("%s", "Impossible to happen\n");
        }
    }
    else{
        printf("Enter a real Age\n");
    }
    return;
}