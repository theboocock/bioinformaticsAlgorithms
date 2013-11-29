#ifndef DYNAMIC_ARRAY_H_
#define DYNAMIC_ARRAY_H_

#include<string.h>
#include<stdlib.h>
#include<stdio.h>

typedef struct dyn_array *string_array;
struct dyn_array{
    int length;
    int size;
    char **items;
};
string_array  new_array(void);
void  append(string_array,char *);
int length(string_array);
void free_array(string_array);
char * get(string_array,int);
void extend(string_array, string_array);
void to_string(string_array);
#endif
