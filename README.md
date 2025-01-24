#include <stdio.h>
#include <string.h>


int main() {

    FILE* fptr;
    fptr=fopen("C:\\Users\\DELL\\Desktop\\DATA\\data.txt.txt","r");
    char Data[100];
    if(fptr==NULL){
        printf("File open unseccessful.");
    }else{
        while(fgets(Data,100,fptr))
           printf("%s\n",Data);
    printf("\nreading is over.");
    }
    fclose(fptr);

    return 0;
