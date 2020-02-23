
clean = "I was happy when my son got 90% marks in his examination ,I was happy when my son got 90% marks in his examination ,True,1,,affection" \
"I went to the gym this morning and did yoga.,I went to the gym this morning and did yoga.,True,1,,exercise"


def generate_grams (clean,n): 
    #Convert to lowercase:
    clean = clean.lower()
    
    #replace non alphanumeric characters with spaces: 
    clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', clean)
    
    # break sentence in token, remove emoty tokens
    tokens = [token for token in clean.split(" ") if token !=""]
    
    # Use zip function to help generate n-grams
    # Concatenate tokens into ngrams and return 
    n_grams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(n_gram) for n_gram in n_grams]

    # Break sentence in the token, remove empty tokens
    tokens = [token for token in clean.split(" ") if token != ""]
    
print(generate_grams(clean, n=1))