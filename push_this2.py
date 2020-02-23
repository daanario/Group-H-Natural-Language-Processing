# -*- coding: utf-8 -*-



import re
with open('trimmed_text.txt', 'r') as f:    # remove \n and then you're done with preprocess 
    text = f.read()



def generate_grams (text,n): 
    #Convert to lowercase:
    text = text.lower()
    
    #replace non alphanumeric characters with spaces: 
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    #break sentence in token, remove emoty tokens
    tokens = [token for token in text.split(" ") if token !=" "]
    
    # Use zip function to help generate n-grams
    # Concatenate tokens into ngrams and return 
    n_grams = zip(*[tokens[i:] for i in range(n)])
    output = [" ".join(n_gram) for n_gram in n_grams]
    #output = list(map(lambda x: x.strip(), output))   
    output = list(map(str.strip,output))
    return output
    
print(generate_grams(text[0:500], n=1))


# try and avoid using lambda (for output)- though it gives the same result 
#as the one with map without lambda

