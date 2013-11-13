import sys


def main():
    dna =sys.stdin.readlines()[0].strip()
    skew = 0
    skews = []
    for c in dna:
        skews.append(skew)
        if c == "G":
            skew += 1
        elif c == "C":
            skew -= 1
            
    skews.append(skew)
    minimum = 0
    indices = []
    for i in range(0,len(skews)):
        if(skews[i] == minimum):
            indices.append(str(i))
        elif(skews[i] < minimum):
            indices =[]
            indices.append(str(i))
            minimum = skews[i]
        
    print(' '.join(indices)) 
if __name__=="__main__":main()
