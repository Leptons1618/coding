#include<stdio.h>

/* Quine */
// // Shorter Version
// int main(){char*c="#include <stdio.h>%cint main(){char*c=%c%s%c;printf(c,10,34,c,34,10);return 0;}%c";printf(c,10,34,c,34,10);return 0;}
// // Longer Version
// static char sym[] = "\n\t\\\"";
 
// int main(void) {
// 	const char *code = "#include <stdio.h>%c%cstatic char sym[] = %c%cn%ct%c%c%c%c%c;%c%cint main(void) {%c%cconst char *code = %c%s%c;%c%cprintf(code, sym[0], sym[0], sym[3], sym[2], sym[2], sym[2], sym[2], sym[2], sym[3], sym[3], sym[0], sym[0], sym[0], sym[1], sym[3], code, sym[3], sym[0], sym[1], sym[0], sym[0], sym[1], sym[0], sym[0]);%c%c%creturn 0;%c}%c";
// 	printf(code, sym[0], sym[0], sym[3], sym[2], sym[2], sym[2], sym[2], sym[2], sym[3], sym[3], sym[0], sym[0], sym[0], sym[1], sym[3], code, sym[3], sym[0], sym[1], sym[0], sym[0], sym[1], sym[0], sym[0]);
 
// 	return 0;
// }
// // Cheating using __FILE__
// // On operating systems where a large range of characters can be used, it is possible to create a Quine by putting the following C code in a file with the same name. 
// main(void){printf(__FILE__);}

/* smallest code in c */ 
// void main(){}

/* how many times the while loop will run */
// int main()
// {
//     int x = 1;
//     while(x++<100){
//         x *= x;
//         printf("%d\n",x);
//         if (x<10)
//             continue;
//         if (x > 50)
//             break;
//         printf("break\n");
//     }
//     return 0;
// }
// /*Output: 3times */





