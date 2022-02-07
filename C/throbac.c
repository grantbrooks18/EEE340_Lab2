/*
C implementations of the Throbac string concatenation function
`__throbac_cat` (provided for you) and the two Throbac built-in
functions `stringlength` and `substring`

Author: Brooks and MacDonald

Version: 2022-01-23
*/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "throbac.h"

char *__throbac_cat(char *first, char *second) {
    size_t length = strlen(first) + strlen(second) + 1;
    void *value = malloc(length);
    if (value == 0) {
        abort();
    }
    strcpy((char *) value, first);
    return strcat((char *) value, second);
}

int stringlength(char *str) {
    return strlen(str);
}

char *substring(char* str, int start, int length) {
    if(start<0){
        printf("\nERROR IN substring()!\nStart is negative.");
        return 0;
    }
    if(length<0){
        printf("\nERROR IN substring()!\nLength is negative.");
        return 0;
    }
    if(start > strlen(str) - 1){
        printf("\nERROR IN substring()!\nStart surpasses string size.");
        return 0;
    }
    if(start + length > strlen(str)){
        printf("\nERROR IN substring()!\nSubstring larger than string.");
        return 0;
    }

    size_t size = length + 1;
    char *sub = malloc(size);
    if (sub == 0) {
        abort();
    }

    for(int i = 0; i < length; i++){
        sub[i] = str[i+start];
    }

    return sub;
}