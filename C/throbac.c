/*
C implementations of the Throbac string concatenation function
`__throbac_cat` (provided for you) and the two Throbac built-in
functions `stringlength` and `substring`

Author: TODO: your names here

Version: 2022-01-23
*/

#include <stdlib.h>
#include <string.h>

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
    // TODO: your code here
}

char *substring(char* str, int start, int length) {
    // TODO: your code here
}
