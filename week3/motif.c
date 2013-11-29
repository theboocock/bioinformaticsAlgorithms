#include "motif.h"

char dna_symbols[] = "ATCG";
void motif_enumeration(string_array dna,string_array results, int k, int d){
    int i,j,l;
    char * kmer = malloc((k+1) * sizeof *kmer);
    char * other_kmer = malloc((k+1) * sizeof *other_kmer);
    //string_array temp;
    for (i = 0; i < strlen(dna->items[0]) - k + 1; i++){
        j = 0;
        while(j < k){
            kmer[j] = dna->items[0][i+j];
            j++;
        }
        kmer[j] = '\0';
        for(j =0; j <= d;j++){
            extend(results,generate_mutations(kmer,d,k)); 
            //printf("%d\n",results->length);
        }  
    }
    free(other_kmer);
    free(kmer);
    //to_string(results);
}

int needle_in_haystack(char * needle,char * haystack,int d,int k){
    int i = 0;
    int mis = 0;
    int j;
    for(i = 0; haystack[i] != '\0'; i++){
        j = 0;
        if(haystack[i] == needle[j++]){
            while(haystack[i+j] == needle[j]) j++;
        }
        if((j - d) >= k){
            return 1;
        }
    }
    return 0;
}

string_array get_combinations(char **mismatches,int choose, int n){
    int i;
    char c[100];
    string_array combinations = new_array();
    for (i = 0; i < n; i++) c[i] = n - i;

    while(1){
        for( i = n;i--;)
            printf("%d%c",c[i],i ? ' ' :'\n');

        if(c[i]++ < choose) continue;
        for (i = 0; c[i] >= choose - i;) if (++i >= n) return combinations;
        for (c[i]++; i; i--) c[i-1] = c[i] + 1;
    } 
    free_array(combinations); 
    return(combinations); 
}


string_array generate_mutations(char * kmer,int d,int k){
    int i,j,l;
    char ** mismatches = malloc(k * sizeof *mismatches);
    int * positions = malloc(k * sizeof *positions);
    string_array mutated_combinations = new_array();
    //printf("%s\n", kmer);
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
        mutated_combinations = get_combinations(mismatches,d,k);  
        

    }
    for (i = 0; i < k; i++){
        free(mismatches[i]);
        printf("blah");
    }
    free(mismatches);
    free(positions);
    return mutated_combinations;
}
