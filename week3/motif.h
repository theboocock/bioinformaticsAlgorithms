#ifndef MOTIF_H_
#define MOTIF_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <math.h>
#include "dynamic_array.h"

extern char dna_symbols[];
void motif_enumeration(string_array,string_array,int k, int d);
string_array generate_mutations(char * kmer,int choose,int n);
string_array get_combinations(char **mismatches,int d, int k);
#endif
