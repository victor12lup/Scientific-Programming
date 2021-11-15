import os
import sys
from string import digits_f, punctuation_f, whitespace_f, lower_case

#filepath = os.path.join('articles','short.txt')

with open(sys.argv[1], 'r', encoding='utf-8', errors='replace') as f:
#f = open(sys.argv[1], 'r', encoding='utf-8', errors='replace')    
    list_1 = []
    list_2 = []
    list_3 = []
    for line in f:        
        
        list_1 = list_1 + line.split()            
    for x in list_1:
            
            str1 = whitespace_f(lower_case(digits_f(punctuation_f(x))))
            if len(str1) > 0 :


                list_2.append(str1)
    # a second for loop is done to correct for some punctuations marks that were left
    # and also new punctuation marks were added to the punctuation_f function
    for x in list_2:
        str1= digits_f(punctuation_f(x))
        if len(str1) > 0:
            list_3.append(str1) 
    print(list_3)
    
    