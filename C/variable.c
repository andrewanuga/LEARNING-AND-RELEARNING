#include <stdio.h>

int main(){
    int level;
    // or int level = 100
    level = 100;

    float height = 170.01;
    double temp = 29.35;

    char alpha = 'A';

    printf("Level: %d\n", level);
    printf("Height %f\n", height);
    printf("Temperature %lf\n", temp);
    // lf ---> Long Float
    // Float uses less storage but is not as precise as double
    print("My Alpha: %c\n", alpha);

    const int num = 20; // constants cannot be changed/reassigned and decalred with const keyword
    // You cannot perform hosting trick on constants they would give an error
    print("Age: %d", num)
    return 0;
}