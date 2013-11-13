import sys
import operator

def get_kmers(dna_string,k):
    kmers={}
    for i in range(0,len(dna_string)-k):
        temp_kmer = dna_string[i:i+k]
        if temp_kmer in kmers:
            kmers[temp_kmer] +=1
        else:
            kmers[temp_kmer] = 1
    s = sorted(kmers.iteritems(),key=operator.itemgetter(1),reverse=True)
    list_of_kmers = []
    max = s[0][1]
    output_kmers = []
    output_kmers.append(s[0][0])
    for i in range(1,len(s)):
        if(max == s[i][1]):
            output_kmers.append(s[i][0])
        else:
            break    
    return output_kmers
         

def main():
    stdinput = sys.stdin.readlines()
    dna_string= stdinput[0]
    k=int(stdinput[1] )
    output = get_kmers(dna_string,k)
    print(' '.join(output))
if __name__=="__main__":main()
