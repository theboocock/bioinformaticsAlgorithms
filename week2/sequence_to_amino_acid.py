# Little library to do amino acid sequencing
#
#
from operator import mul
gencode = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*',
    'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W'}

tyrocidine_B1 = 'VKLFPFNQY'
def sequence_to_amino_acid(dna_string):
    return ''.join([gencode.get(''.join(x)) for x in zip(dna_string[0::3],dna_string[1::3],dna_string[2::3])]).strip("*")

def count_combinations():
    tyrocidine_B1 = 'VKLFPFNQY'
    o_n_dict = {}
    combinations = []
    for codon, amino in gencode.items():
        try:
            o_n_dict[amino] += 1
        except KeyError:
            o_n_dict[amino] = 1
    for c in tyrocidine_B1:
        combinations.append(o_n_dict[c])
    print(type(combinations))
    product = 1
    for a in combinations:
       product *= a
    print(product) 

def factorial(n):
    if ( n == 1):
        return 1
    else:
        return n * factorial(n-1)
def __rev_dna__(base):
    if base == "A":
        return "T"
    elif base =="G":
        return "C"
    elif base =="C":
        return "G"
    else:
        return "A"

    
def __get_rna__(base):
    if base == "T":
        return "U"
    return base

def __get_dna__(base):
    if base == "U":
        return "T"
    return base

def chunks(l,n):
    
    for i in range(0,len(l)-n+1,n):
        yield l[i:i+n]
def convert_chunks_to_amino_acid(chunks):
    out_amino = ''
    for chunk in chunks:
        chunk = ''.join(chunk)
        out_amino += gencode[chunk]
    return (out_amino)


def open_peptide_file(input_file):
    with open(input_file,'r') as f:
        lines=f.readlines()
        dna_sequence = lines[0].strip()
        amino_acid_sequences = lines[1].strip()
    return(dna_sequence,amino_acid_sequences)

def peptide_encoding_problem(dna_sequence,amino_acid_sequences):
    rna_sequence = list(map(__get_rna__,dna_sequence))
    rev_rna = list(map(__get_rna__,map(__rev_dna__,dna_sequence)))[::-1]
    for reading_frame in range(3):
        fwd_search =convert_chunks_to_amino_acid(chunks(rna_sequence[reading_frame:],3))
        rev_search = convert_chunks_to_amino_acid(chunks(rev_rna[reading_frame:],3))
        fwd_results = needle_in_haystack(amino_acid_sequences,fwd_search,reading_frame)
        rev_results =needle_in_haystack(amino_acid_sequences,rev_search,reading_frame)
        for a in fwd_results:
            a = (a) * 3 + reading_frame
            print(''.join(list(map(__get_dna__,rna_sequence[a:a+len(amino_acid_sequences)*3]))))
        for a in rev_results:
            a = len(rna_sequence) - ((a) * 3 + reading_frame)
            print(''.join(list(map(__get_dna__,rna_sequence[a-len(amino_acid_sequences)*3:a]))))

def needle_in_haystack(pattern,haystack,t): 
    matches = []
    needle = pattern[0]
    for i,c in enumerate(haystack):
        index = 1 
        if( c == needle): 
          for j in range(i+1,i + len(pattern)):
            if (j >= len(haystack)):
                break
            if (haystack[j] != pattern[index] ):
                break
            index +=1 
        if(index == len(pattern)):
            matches.append(i)
    return(matches) 
