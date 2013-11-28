#include "dynamic_array.h"


string_array new_array(){
    string_array array;
    array = malloc(sizeof *array);
    array->length = 0;
    array->size = 2;
    array->items = malloc(array->size * sizeof *(array->items));
    return array;
}

void append(string_array array,char * item){
    if(array->length == array->size){
        array->items = realloc(array->items,(array->size * 2) * sizeof *(array->items));
        array->size *=2;
    }
    array->items[array->length] = malloc((strlen(item) + 1) * sizeof *item);
    strcpy(array->items[array->length++],item);
}

int length(string_array array){
    return array->length;
}

void free_array(string_array array){
    int i;
    for( i= 0; i < array->length; i++){
        free(array->items[i]);
    }   
    free(array->items); 
    free(array);
}

char * get(string_array array,int i){
    return array->items[i];
}

