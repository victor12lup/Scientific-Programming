#Victor Salazar
#12061468
import os
import sys
import csv
from string import digits_f, punctuation_f, whitespace_f, lower_case
from collections import defaultdict
from collections import Counter
from functional import my_map, my_filter, my_reduce

# Openning each file called by sys.argv[1]
with open(sys.argv[1], 'r', encoding='utf-8', errors='replace') as f:
    list_1 = []
    list_2 = []
    list_3 = []
    #Create a list with all the words of the file
    for line in f:        
        
        list_1 = list_1 + line.split()            
    # Clean , correct and convert to lower case
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

# Use os for reaching all the articles and data files required 

for (root, dirs, files) in os.walk('data/unigram'):
    categories = []
    dictionary = defaultdict(dict)
    # Create a list with all the ctaegories and open each of it 
    for file in files:
        m = file.strip('.csv')
        categories.append(m)
        # Here we open each article and create a nested dictionary 
        with open(os.path.join(root, file), 'r', encoding='utf-8', errors='replace') as csvfile:
            rdr = csv.reader(csvfile)
            # dictionary is in this form {cegory:{unigram:score}}
            for row ,number in rdr:  
                dictionary[m][row] = number
            
# This function will get the values of the dictionary of a certain word x 
def get(x):
    return int(dictionary[dicto].get(x,0))


# Create a dictionary for scores of each category

score = defaultdict(int)
for dicto in categories: 
    #results_lambda_function = my_filter(lambda x: x in dictionary[dicto][x], list_3)
    # Create a list with my map , use the function get and the list to have a list of scores
    scores =my_map(get,list_3)
    score[dicto] += sum(scores)
    
# Sort and print the top 5 categories in dict score    
final = Counter(score)
k = final.most_common(5)
for i in k:
    print(i[0], "=" ,i[1])
       
  
        
        