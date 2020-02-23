
import re
with open('trimmed_text.txt', 'r') as f:    
    text = f.read()


def generate_grams (text,n): 
    #Convert to lowercase:
    text = text.lower()
    
    #replace non alphanumeric characters with spaces: 
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    #break sentence in token, remove emoty tokens
    tokens = [token for token in text.split(" ") if token !=" "]
    
    # Use zip function to help generate n-gram
    # Concatenate tokens into ngrams and return 
    n_grams = zip(*[tokens[i:] for i in range(n)])
    output = [" ".join(n_gram) for n_gram in n_grams]
    #output = list(map(lambda x: x.strip(), output))    
    output = list(map(str.strip,output))    # Strips '\n' from end of sentences
    return output
    
print(generate_grams(text, n=1))

