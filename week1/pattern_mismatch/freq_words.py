import sys
import itertools

def hamming_distance(s1, s2):
    "Return the Hamming distance between equal-length sequences."
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def revdna(dna):
    rev = ''
    for c in dna:
        if c == "G":
            rev +="C"
        elif c =="A":
            rev += "T"
        elif c =="T":
            rev += "A"
        else:    
            rev += "G"
    return(rev[::-1])

def get_mutated(word, num_mismatches):
    letters = "ATCG"
    for locs in itertools.combinations(range(len(word)), num_mismatches):
        this_word = [[char] for char in word]
        for loc in locs:
            orig_char = word[loc]
            this_word[loc] = [l for l in letters if l != orig_char]
        for poss in itertools.product(*this_word):
            yield ''.join(poss)

def get_kmers(dna,k,d):
    kmers = []
    for e in itertools.product('ATCG',repeat=k):
        kmers.append(''.join(e))
    output_mutated_kmers = {}
    kmers_real_data = []
    rev_comp_dna = []
    output_rev_comp =  {}
    for i in range(len(dna) -k + 1):
        kmers_real_data.append(dna[i:i+k])
    for i in range(len(dna) - k + 1):
        rev_comp_dna.append(revdna(dna[i:i+k])) 
    for i in range(len(kmers_real_data)):
        for mm in range(0,d+1):
            mutators = get_mutated(kmers_real_data[i],mm)       
            rev_mutators = get_mutated(kmers_real_data[i],mm)
            for mutant in mutators:
                    try:
                        output_mutated_kmers[mutant] +=1 
                    except KeyError:
                        output_mutated_kmers[mutant] = 1
            for rev_mutator in rev_mutators:
                    try:
                        output_rev_comp[rev_mutators] +=1
                    except KeyError:
                        output_rev_comp[rev_mutators] = 1


    return(output_mutated_kmers,output_rev_comp)
 

def main():
    input_stdin = sys.stdin.readlines()
    dna = input_stdin[0].strip()
    second = input_stdin[1].strip().split()
    k = int(second[0])
    d = int(second[1])
    (out,rev_comp) = get_kmers(dna,k,d)
    try:
        maximum = next (iter (out.values()))
        maximum += rev_comp[revdna((next (iter(out))))]
    except KeyError:
        maximum = next (iter (out.values()))
    outs = []
    for item in out:
        try:
            temp_max = out[item]
            temp_max += out[revdna(item)]
        except KeyError:
            temp_max = out[item]
            
        if(maximum == temp_max):
            if(item not in outs):
                outs.append(item)
            if(revdna(item) not in outs):
                outs.append(revdna(item))
        elif(maximum < temp_max):
            maximum = temp_max
            outs = []
            if(item not in outs):
                outs.append(item)
            if(revdna(item) not in outs):
                outs.append(revdna(item))
        
    print(maximum)
    print('\n'.join(outs))   
if __name__=="__main__":main()
    
    
