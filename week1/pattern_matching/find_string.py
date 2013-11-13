import os
import sys

def main():
    inString = sys.stdin.readlines()
    pattern = list(inString[0].strip())
    haystack = list(inString[1].strip())
    needle = pattern[0]
    index = 0 
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
            print(i,end=' ')
    print()
    

if __name__=="__main__":main()
