import sys
import itertools

def hamming_distance(s1, s2):
    "Return the Hamming distance between equal-length sequences."
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


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
    for i in range(len(dna) -k + 1):
        kmers_real_data.append(dna[i:i+k]) 
    for i in range(len(kmers_real_data)):
        for mm in range(0,d+1):
            mutators = get_mutated(kmers_real_data[i],mm)        
            for mutant in mutators:
                    try:
                        output_mutated_kmers[mutant] +=1 
                    except KeyError:
                        output_mutated_kmers[mutant] = 1
    return(output_mutated_kmers)
 

def main():
    input_stdin = sys.stdin.readlines()[0].strip().split()
    dna = input_stdin[0]
    k = int(input_stdin[1])
    d = int(input_stdin[2])
    out = get_kmers(dna,k,d)
    maximum = next (iter (out.values()))
    outs = []
    for item in out:
        if(maximum == out[item]):
            outs.append(item)
        elif(maximum < out[item]):
            maximum = out[item]
            outs = []
            outs.append(item)
    print(maximum)
    print('\n'.join(outs))   
if __name__=="__main__":main()
    
    
