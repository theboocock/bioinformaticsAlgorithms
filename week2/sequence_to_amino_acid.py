# Little library to do amino acid sequencing
#
#
from operator import mul
import operator
    
from collections import OrderedDict                 
int_mass_table = {
    'G':57, 'A':71, 'S':87, 'P':97,
    'V':99, 'T':101, 'C':103, 'I':113,
    'L':113, 'N':114, 'D':115, 'K':128,
    'Q':128, 'E':129, 'M':131, 'H':137,
    'F':147, 'R':157, 'Y':163, 'W':186}

reduced_mass_table = {
    'G':57, 'A':71, 'S':87, 'P':97,
    'V':99, 'T':101, 'C':103,
    'I':113, 'N':114, 'D':115, 'K':128,
    'E':129, 'M':131, 'H':137,
    'F':147, 'R':156, 'Y':163, 'W':186}
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

def abs(a,b):
    total =a - b
    if (total > 0):
        return total
    else:
        return -total
def convulution_cyclopeptide_ping(spectrum,m,n):
    masses = get_top_m_massese(spectrum,m)
    

def get_top_m_massese(spectrum,m):
    spectrum = sorted(spectrum)
    masses = {}
    for i in range(len(spectrum)):
        for j in range(i+1,len(spectrum)):
            result = abs(spectrum[i],spectrum[j])
            if(result <= 200 and result >= 57):
                try:
                    masses[result] +=1 
                except KeyError:
                    masses[result] = 1
    masses = sorted(masses.items(),key=lambda x: x[1],reverse=True)
    m_index =0
    return_masses = []
    prev_mass = 0
    for i in range(len(masses)):
        print(masses[i][1])
        if(m_index < m):
            return_masses.append(masses[i][0])
        elif(masses[i][0] == prev_mass):
            return_masses.append(masses[i][0])
        else:
            break
        m_index += 1

        prev_mass = masses[i][0]
    return(return_masses)
       


def convultion_cyclopeptide_sequencing(spectrum,masses,N):
    leader_peptide = [0]
    leader_beard = [[0]]
    j= 0
    while(len(leader_beard) > 0):
        expand_peptides=list(leader_beard)
        leader_beard = []
        for item in expand_peptides:
            for mass in masses:
                t_start_pep=list(item)
                t_start_pep.append(mass)
                leader_beard.append(t_start_pep)
        for i, peptide in enumerate(list(leader_beard)):
            peptide_cyclo_spectrum = get_cyclo_peptide_spectrum(peptide)
#            if(72 in peptide_cyclo_spectrum):
#                print(peptide)
            if(peptide_cyclo_spectrum[len(peptide_cyclo_spectrum)-1] == spectrum[len(spectrum)-1]):
                    leader_peptide = peptide
            elif(peptide_cyclo_spectrum[len(peptide_cyclo_spectrum)-1] > spectrum[len(spectrum)-1]):
                leader_beard.remove(peptide)
        if(len(leader_beard) == 0):
            break
        leader_beard = cut(leader_beard,spectrum,N)
        print(len(leader_beard))
    print('-'.join([str(o) for o in leader_peptide[1:]]))

def get_pairwie_positive(cyclo):
    cyclo=sorted(cyclo)
    print(cyclo)
    sampling_list=[]
    for i in range(len(cyclo)):
        for j in range(i+1,len(cyclo)):
            result = abs(cyclo[i],cyclo[j])
            if(result != 0):
                sampling_list.append(result)
    return(' '.join([str(o) for o in sorted(sampling_list)]))
     


def get_spectral_convulution(spectrum):
    generate_distances = get_pairwie_positive(cyclo_spec)
    print(generate_distances)
    

def get_spectrum(input_spectrum):
    return [int(o) for o in input_spectrum.split()]
    



def get_cyclo_peptide_spectrum(peptide):
    peptide = list(peptide)
    peptide.remove(0)
    cycl = [0]
    for i, item in enumerate(peptide):
        total = 0 
        for j in range(i+1,i +1 + len(peptide)-1):
            index = j % len(peptide)
            total+= peptide[index]
            cycl.append(total)
    total = 0
    for item in peptide:
        total += item
    cycl.append(total)
    return cycl 
    
def score(peptide,spectrum):
    count = 0
    peptide = sorted(list(peptide))
    spectrum = sorted(list(spectrum))
    s_index = 0
    p_index = 0
    while(p_index< len(peptide) and s_index < len(spectrum)):
        p = peptide[p_index]
        s = spectrum[s_index]
        if(p == s):
            count +=1
            p_index +=1
            s_index +=1
        elif (p > s):
            s_index+=1
        else:
            p_index+=1
    return count

def cut(leader_beard,spectrum,N):
    scores=[]
    for leader in leader_beard:
        scores.append(score(get_cyclo_peptide_spectrum(leader),spectrum))
        
    sorted_scores = sorted(zip(scores,leader_beard),key=lambda t:t[0],reverse=True)
    first_score = sorted_scores[0][0]
    resulting_leader_beard=[sorted_scores[0][1]]
    for i in range(1,len(sorted_scores)):
        current_score = sorted_scores[i][0]
        if(current_score == first_score):
            resulting_leader_beard.append(sorted_scores[i][1])
        elif(i > N):
            break
        else:
            resulting_leader_beard.append(sorted_scores[i][1])
        first_score = current_score
    return resulting_leader_beard 
 

def leader_board_cyclopeptide_sequencing(spectrum,N):
    leader_peptide = [0]
    leader_beard = [[0]]
    j= 0
    while(len(leader_beard) > 0):
        expand_peptides=list(leader_beard)
        leader_beard = []
        for item in expand_peptides:
            for mass in reduced_mass_table.values():
                t_start_pep=list(item)
                t_start_pep.append(mass)
                leader_beard.append(t_start_pep)
        for i, peptide in enumerate(list(leader_beard)):
            peptide_cyclo_spectrum = get_cyclo_peptide_spectrum(peptide)
            if(peptide_cyclo_spectrum[len(peptide_cyclo_spectrum)-1] == spectrum[len(spectrum)-1]):
                if(score(peptide_cyclo_spectrum,spectrum) > score(get_cyclo_peptide_spectrum(leader_peptide),spectrum)):
                    leader_peptide = peptide
            elif(peptide_cyclo_spectrum[len(peptide_cyclo_spectrum)-1] > spectrum[len(spectrum)-1]):
                leader_beard.remove(peptide)
        if(len(leader_beard) == 0):
            break
        leader_beard = cut(leader_beard,spectrum,N)
    print('-'.join([str(o) for o in leader_peptide[1:]]))
            
# cyclopeptide sequencing 
def read_spectrum(f):
    with open(f,'r') as file_name:
        spectrum = file_name.readlines()[0].strip()
        return([int(o) for o in spectrum.split()])
#
# returns -1 when inconsistent
# returns 0 when consistent
# returns 1 when consistent and complete       

def peptide_consistent(peptide,spectrum):
    spectrum_length = len(spectrum)
    spectrum = list(spectrum)
    #remove the zero peptides
    peptides_removed = 0
    for i, first in enumerate(peptide):
        total = 0
        for j in range(i+1,len(peptide)):
            total += peptide[j]
            try:
                spectrum.remove(total)
                peptides_removed += 1
            except ValueError:
                return -1
    #print(peptide)
    #print(len(peptide))
    #print((len(peptide)-1) * (len(peptide) - 2) +2)
    #print(len(spectrum))
    if(((len(peptide)-1) * (len(peptide) - 2) +2) == spectrum_length):
        #print("wow")
        return 1
    return 0
        
def cyclopeptide_sequencing(spectrum):
    peptides=[[0]]
    while(len(peptides) > 0):
            peptide = peptides.pop()
            #print(peptide)
            #print(spectrum)
            for mass in reduced_mass_table.values():
                temp_peptide = list(peptide)
                temp_peptide.append(mass)
                check_match =  peptide_consistent(temp_peptide,spectrum)
                if(check_match == 1):
                    print("-".join([str(o) for o in temp_peptide][1:]))
                elif(check_match == 0):
                    # add peptide to list
                    peptides.append(temp_peptide)

def open_amino_acid(f):
    with open(f,'r') as file_name:
        amino_acid_sequence=file_name.readlines()[0].strip() 
        return amino_acid_sequence

def get_mass(f):
    with open(f,'r') as file_name:
        mass_integer=int(file_name.readlines()[0].strip())
        return(mass_integer)  

coins = [1,2,3,4,5]
big_map={}
def get_peptide_mass_coins(n):
    total = 0
    #print(n)
    if n == 0:
        return 1
    if n < 0:
        return 0
    for value in coins:
        total += get_peptide_mass_coins(n-value)
    return total
def get_peptide_mass(n,depth):
    total = 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n not in big_map:
        for key,value in reduced_mass_table.items():
            temp_answer = n -value
            total += get_peptide_mass(temp_answer,depth+1)
            if depth == 0:
                print(get_peptide_mass(temp_answer,depth+1))
                print(key)
                print("====")
        big_map[n] = total
    else:
            total = big_map[n]
    return total
def get_peptide_mass_rec(n):
    total = 0
    #print(n)
    if n == 0:
        return 1
    if n < 0:
        return 0
    for key,value in reduced_mass_table.items():
        total += get_peptide_mass_rec(n-value)
    return total

def recursive_peptides(get_mass):
    return(get_peptide_mass(get_mass))

def mass_table(amino_acid_string):
    theoretical_spectrum=[]
    theoretical_spectrum.append(0)
    for i in range(len(amino_acid_string)):
        ########3
        temp_mass = int_mass_table[amino_acid_string[i]]
        theoretical_spectrum.append(temp_mass)
        for j in range(i + 1,i + len(amino_acid_string)-1):
           index = j % len(amino_acid_string)
           temp_mass += int_mass_table[amino_acid_string[index]]
           theoretical_spectrum.append(temp_mass)
    theoretical_spectrum.append(temp_mass + int_mass_table[amino_acid_string[(j+1) % len(amino_acid_string)]]) 
    theoretical_spectrum = ' '.join([str(o) for o in sorted(theoretical_spectrum)])
    #blah
    return(theoretical_spectrum) 

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
