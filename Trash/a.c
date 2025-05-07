#include <stdio.h>

void func(){
    printf("Hello, World!\n");
}

int main(){
    int i = 0;
    for(i = 0; i < 5; i++){
        func();
    }   
}