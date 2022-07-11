#include <stdio.h>

int factorial(int num);
int main() {
    char a;
    for (;;) {
        scanf(" %c", &a);
        a = a - '0';
        if (a == 65) {
            break;
        }
        else {
            printf("%d\n", factorial(a));
        }
    /* by converting the char to ascii */
    // for (;;) {
    // scanf(" %c", &a);
    // a = (int)(a);
    // if (a == 113) {
    //     break;
    // }
    // else {
    //     printf("%d\n", factorial(a = a - '0'));
    // }
    }
    return 0;
}
int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}
