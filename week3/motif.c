#include "motif.h"

char dna_symbols[] = "ATCG";
void motif_enumeration(string_array dna,string_array results, int k, int d){

    int i,j,count,l,t;
    char * kmer = malloc((k+1) * sizeof *kmer);
    char * other_kmer = malloc((k+1) * sizeof *other_kmer);
    string_array mutated = new_array();
    for( t = 0; t < dna->length; t++){
        for (i = 0; i < strlen(dna->items[k]) - k + 1; i++){
            j = 0;
            while(j < k){
                kmer[j] = dna->items[t][i+j];
                j++;
            }
            kmer[j] = '\0';
            for(l=0; l <= d; l++){
                extend(mutated,generate_mutations(kmer,l,k));
            }
    //        to_string(mutated);
            for(l = 0; l < mutated->length; l++){ 
                count = 0;
                for(j =0; j < dna->length;j++){
                        if(needle_in_haystack(get(mutated,l),get(dna,j),d,k)){
                            count++;
                        }
                }
                if(count == (dna->length)){
                    unique_append(results,get(mutated,l));
     //             to_string(results);
                }
            }
    }
    }
    to_string(results);
    free(other_kmer);
    free(kmer);
    free_array(mutated);
    //to_string(results);
}

int needle_in_haystack(char * needle,char * haystack,int d,int k){
    int i = 0;
    int mis = 0;
    int j;
    int len = strlen(haystack);
    for(i = 0; len -k + 1 ; i++){
        j = 0;
        while(j < k){ 
            if(haystack[i+j] == needle[j]){
                mis++;
            }
            j++;  
        }
        if((j+i) > len && mis < k){
          //  printf("j = %s %s  \n",needle,haystack);
            return 0;
        }
        if((mis + d ) >= k){
           //printf("%s %d %s %d %d\n",needle,mis,haystack,j,len);
            return 1;
        }
        mis = 0;
    }
    return 0;
}

void get_product(char * kmer,string_array combinations,char** mismatches,int *pos,int n){
    int i,j,k,l;
    int *c;
    char * temp_kmer = malloc((strlen(kmer)+1) * sizeof *kmer);
    for(i = 0; kmer[i] != '\0';i++){
        temp_kmer[i] = kmer[i];
    }
    temp_kmer[i] = '\0';
    c = malloc(n * sizeof *c);
    for(i = 0; i < n;i++) c[i] = 0;
    i = n -1;
    j  = 0;
    
    while(1){
        while(c[i] <3){
            for(k=0; temp_kmer[k] != '\0';k++){
                temp_kmer[k] = kmer[k];
            }
            //printf("%d pos k\n",pos[0]);
            for(k=0;k<n;k++){
             //   printf("%d ",c[k]);
                temp_kmer[pos[k]] = mismatches[pos[k]][c[k]];
            }
            //printf("\n");
            //printf("%s\n",temp_kmer);
            append(combinations,temp_kmer);
            c[i] +=1; 
            //printf("c[i] = %d i = %d\n",c[i],i); 
        }        

        if(c[0] == (3)) break;
        //printf("j == %d\n",j);
        //fflush(stdout);
        if(c[i-j] == (3)){
            j++;
        }
        c[i-j]++;
        for(k = (i-j) + 1; k <= i; k++){
            c[k] = c[k-1];
        }
    }
    free(c);
    free(temp_kmer);
} 


string_array get_combinations(char * kmer,char **mismatches,int choose, int n){
    int i,j,k;
    int *c;
    c = malloc(choose* sizeof * c);
    string_array combinations = new_array();
    for (i = 0; i < choose; i++) c[i] = i;
    i = choose -1;
    j = 0;
    //printf("choose = %d n = %d \n",choose,n);
    while(1){
        while(c[i] < (n)){
            for(k=0; k < choose;k ++){
      //          printf("%d ",c[k]);
            }
        //    printf("\n");
            get_product(kmer,combinations,mismatches,c,choose);
            c[i] += 1;
        }
        if(c[0] == (n - choose  + 1)){;
            break;
        }
        if(c[i-j] == (n-j)){
            j++;
        }
        c[i-j]++;
        for(k = (i-j) + 1; k <= i; k++){
            c[k] = c[k-1] + 1;
            }
        }
    free(c);
    return(combinations); 
}


string_array generate_mutations(char * kmer,int d,int k){
    int i,j,l;
    char ** mismatches = malloc(k * sizeof *mismatches);
    int * positions = malloc(k * sizeof *positions);
    string_array mutated_combinations = new_array();
    
    if(d == 0){
        append(mutated_combinations,kmer);
    }else{
        for (i = 0; i < k; i++){
            mismatches[i] = malloc(4 * sizeof **mismatches); 
            j = 0;
            l = 0;
            while(j < 4){
                if(kmer[i] != dna_symbols[j]){
                   mismatches[i][l++] = dna_symbols[j]; 
                }
                j++;
            }
            mismatches[i][l++] = '\0';
        }
        
        // generate all combinations of mismatches.    
        extend(mutated_combinations,get_combinations(kmer,mismatches,d,k)); 
        for (i = 0; i < k; i++){
            free(mismatches[i]);
        }

    }
    free(mismatches);
    free(positions);
    return mutated_combinations;
}
