import sys
from sequence_to_amino_acid import sequence_to_amino_acid

dna = sys.stdin.readlines()[0]
print(sequence_to_amino_acid(dna))


