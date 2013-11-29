#include "motif.h"


int main(int argc, char *argv[]){
    FILE *input;
    
    int k= 0, d = 0, i;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
 
    char *token=NULL, *cp=NULL;
    const char delim[] = " ";
    string_array dna = new_array();
    string_array results = new_array();
    if(argc != 2){
        fprintf(stderr,"No file specified on command line\n");
        return EXIT_FAILURE;
    }
    input = fopen(argv[1],"r");
    i = 0;
    while((read = getline(&line,&len,input)) != -1){
        if( i > 0 ){
            append(dna,strtok(line,"\n"));
        }else{
            cp = strdup(line);
            token = strtok(cp,delim);
            k = atoi(token);
            token = strtok(NULL,delim);
            d = atoi(token);
        }
        i++;
    }
    motif_enumeration(dna,results,k,d);
    free(line); 
    fclose(input);
    free(cp); 
    free_array(dna);
    free_array(results);
    return EXIT_SUCCESS;
}
