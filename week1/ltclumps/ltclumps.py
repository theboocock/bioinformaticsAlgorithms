import sys
import operator

def get_kmers(dna_string,k,t,L):
    kmers={}
    for i in range(0,len(dna_string)-k):
        temp_kmer = dna_string[i:i+k]
        try:
            kmers[temp_kmer][0] +=1
            kmers[temp_kmer][1].append(i)
        except KeyError:
            kmers[temp_kmer] = [1,[i]]
    list_of_kmers = []
    output_kmers = []
    i = 0
    for item in kmers:
        if(kmers[item][0] >=t):
            if(any_t_kmers(kmers[item][1],L,t,k)):
                    output_kmers.append(item)       
        i += 1
    return output_kmers


def any_t_kmers(indices,L,t,k):
    t = t -1
    for i in range(0,len(indices) - t):
        if(indices[i+t] -indices[i] <= L-k):
        #    print(L)
        #    print(indices[i+t] - indices[i])
            return True 
    return False

def main():
    line = sys.stdin.readlines()
    input_dna = line[0]
    parameters=line[1].split()
    k=int(parameters[0])
    L=int(parameters[1])
    t=int(parameters[2])
    output_kmers = []
    output_kmers = get_kmers(input_dna,k,t,L)
    valid_kmers = []
    print(' '.join(output_kmers))


if __name__=="__main__":main()
