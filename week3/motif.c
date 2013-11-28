#include "motif.h"

void motif_enumeration(string_array dna,string_array results, int k, int d){
    int i;
    for (i = 0; i < dna->length; i++){
        printf("%s\n",get(dna,i));
    }
    

}
