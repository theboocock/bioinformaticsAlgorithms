import sys

def main():
    input_stdin = sys.stdin.readlines()
    pattern = input_stdin[0].strip()
    dna = input_stdin[1].strip()
    d = int(input_stdin[2].strip())
    output_pos = []
    #print(d)
    #print(len(pattern))
    #print(len(dna))
    for i in range(0, len(dna)-len(pattern)+d):
        test_string = dna[i:i+len(pattern)]
        #print(len(test_string))
        #print(len(pattern))
        count_mismatch = 0
        for j in range(0,len(test_string)):
            if(test_string[j] != pattern[j]):
                count_mismatch += 1
            if(count_mismatch > d):
                break     
        count_mismatch += len(pattern) - len(test_string)
        if(count_mismatch <=d):
            output_pos.append(str(i))
    #print(len(test_string))
    print('\n'.join(output_pos))
if __name__=="__main__":main()
