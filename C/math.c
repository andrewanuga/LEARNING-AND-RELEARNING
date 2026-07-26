#include <stdio.h>

int main(){
    const int x = 10;
    const int y = 14;
    
    int ans = x + y;
    
    printf("My_Ans: %d\n", ans);
    
    return 0;
}

int multi(){
    const int x = 10;
    const int y = 41;
    
    multiply = x*y;

    printf("Multi %d\n", multiply);

    return 0; // if u do not add return statemnt the compiler automatically add return 0
}

int div(){
    const int num1 = 10;
    const int num2 = 5;

    int ans = num1 / num2;

    printf("Div: %f\n", ans);
    return 0;
}

int mod(){
    const int x = 10;
    const int y = 4;

    int modu= x % y;
    printf("Remain: %d\n", modu);

    return 0;
}