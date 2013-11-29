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


void extend(string_array a, string_array b){
    int i;
    int nearest_power_two = 1;
    int sum;
    if(b->length ==0){
        return;
    }
    sum = a->length + b->length;
    while( sum >>= 1){
        nearest_power_two <<= 1;
    }
    nearest_power_two <<= 1;
    a->items = realloc(a->items,(nearest_power_two * sizeof *(a->items)));
    a->size = nearest_power_two;
    for (i = a->length; i < (a->length + b->length); i++){
        a->items[i] = b->items[i-a->length]; 
    }
    a->length += b->length;
    printf("%d\n",a->length);
    if(a->items != b->items){
        free(b->items);
    }
    if(a != b){
        free(b);
    }
}

void to_string(string_array a){
    int i;
    for( i = 0; i < a->length; i++){
        printf("%s\n",a->items[i]);
    }
}

