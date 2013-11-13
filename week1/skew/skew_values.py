import sys




def main():
    input_dna = sys.stdin.readlines()[0]
    skew = 0
    skews = []
    i = 0
    for c in input_dna:
        print(skew,end=' ') 
        if c == "G":
            skew += 1
        elif c == "C":
            skew -= 1
        i += 1
 
if __name__=="__main__":main()
