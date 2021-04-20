## NATURAL LANGUAGE UNDERSTANDING
## ASSIGNMENT 1 - DEPENDENCY PARSING


import spacy

nlp = spacy.load('en_core_web_sm')


## Exercise 1

def path_root_token(sentence): 

    # The function outputs the path of dependency relations
    # from the root to each token of the sentence.
    # :param sentence: a tokenized sentence
    # :return: the dictionary of paths from the root to each token

    # Initialize an empty dictionary
    paths = dict()

    # Iterate over the tokens of the tokenized sentence
    for token in doc:

        # Initialize an empty list at the token's key
        paths[token] = list()

        # Retrieve the ancestors of the token
        ancestors = token.ancestors

        # Iterate over the ancestors
        for a in ancestors:
            info = dict()

            # Extract the syntactic dependency relation 
            info[a.dep_] = a
            paths[token].append(info)

        # Reverse the values of the nested dictionary
        paths[token].reverse()

    return(paths)



## Exercise 2

def extract_subtree(sentence):

    # The function extracts the subtree of dependencies
    # from each token of a given sentence.
    # :param sentence: a tokenized sentence
    # :return: a list of lists, each containing the subtree
    #          of each token of a sentence

    subs = list()

    # Iterate over all tokens
    for token in doc:

        # Append the subtree of the token to the list
        subs.append(list(token.subtree))

    return(subs)



## Exercise 3

def compare(token_list, string_list):
    
    # The function compares a spacy object spacy.tokens.token.Token
    # with a a given list of tokens of type list. 
    # :param token_list: list of tokens
    # :param string_list: list of split string
    # :return: bool True -> the two lists contain the same objects
    #          bool False -> the two lists do not contain the same objects

    # Ensure that the two lists have same length
    if len(token_list) != len(string_list):
        return False
    
    # If they have the same length...
    else:
        # ...iterate over the length of the lists
        for i in range(len(token_list)-1):

            # If at least one word is different, return False
            if token_list[i] != string_list[i].text:
                return False
    
    return True


def check_subtree(sentence, token_list):

    # The function checks whether a given list of tokens
    # forms a subtree or not.
    # :param sentence: a tokenized sentence
    # :param token_list: list of split string
    # :return: bool True -> the tokens list forms a subtree
    #          bool False -> the tokens list does not form a subtree

    # Call the extract_subtree() function over the input
    give_subtree_sent = extract_subtree(sentence)

    # Iterate over the subtrees
    for e in give_subtree_sent:

        # Check if the subtree is equal to the tokens list
        # by calling the compare() function
        if(compare(token_list, e)):
            return True

    return False



## Exercise 4

def get_head_span(span):

    # The function identifies the head of a span given its tokens.
    # :param span: a tokenized span
    # :return: the head of the span

    # Initialize an empty dictionary 
    child_nodes = dict()

    # Iterate over the tokens of the tokenized sentence
    for token in doc:

        # Initialize an empty list at the token's key
        child_nodes[token] = []

        # Retrieve the children of the token
        children = token.children

        #Iterate over the children
        for c in children:
            info = dict()

            ## Extract the syntactic dependency relation 
            info[c.dep_] = c
            child_nodes[token].append(info)

        # Reverse the values of the nested dictionary
        child_nodes[token].reverse()

    # Sort the dictionary according to decreasing number 
    # of children for each token
    head_span = sorted(child_nodes, key=lambda k: len(child_nodes[k]), reverse = True)

    # Retrieve the head of the span by extracting
    # the token with the highest number of children
    return(head_span[0])



## Exercise 5

def subj_obj_span(sentence):

    # The function extracts the sentence subject, direct
    # object and indirect object spans.
    # :param sentence: a tokenized sentence
    # :return: a dictionary containing the spans of subject,
    #          direct object and indirect object

    # Initialize a dictionary with keys of interest
    spans = {'nsubj': [], 'dobj':[], 'pobj': []}

    # Iterate over the tokens of the tokenized sentence
    for token in sentence:
        
        # Check if the syntactic dependency relation of the token is nsubj
        if token.dep_ == 'nsubj':

            # Initialize a list for storing descendants
            desc = list()

            # Iterate over descendants
            for d in token.subtree:
                desc.append(d.text)

            # Append the joined tokens to the correct entry in the dict
            spans['nsubj'].append(' '.join(desc))

        # Check if the syntactic dependency relation of the token is dobj
        elif token.dep_ == 'dobj':

            # Initialize a list for storing descendants
            desc = list()

            # Iterate over descendants
            for d in token.subtree:
                desc.append(d.text)

            # Append the joined tokens to the correct entry in the dict
            spans['dobj'].append(' '.join(desc))

        # Check if the syntactic dependency relation of the token is pobj
        elif token.dep_ == 'pobj':

            # Initialize a list for storing descendants
            desc = list()

            # Iterate over descendants
            for d in token.subtree:
                desc.append(d.text)

            # Append the joined tokens to the correct entry in the dict 
            spans['pobj'].append(' '.join(desc))
    
    return(spans)




## TESTING

sent = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(sent)


## Exercise 1
result1 = path_root_token(doc)
print('Path from ROOT to each token of sentence:')
print('{}\t{}'.format('Token', 'Path from ROOT'))
print('-' * 50)
for key, value in result1.items():
    print('{}\t{}'.format(key, value))
print('\n')


## Exercise 2
result2 = extract_subtree(doc)
print('Subtree for each token:')
print('{}\t{}'.format('Token', 'Subtree'))
print('-' * 50)
for token, subtree in zip(sent.split(), result2):
     print('{}\t{}'.format(token, subtree))
print('\n')


## Exercise 3
token_list = ['buying', 'U.K.']
result3 = check_subtree(doc, token_list)
if result3 == True: 
    print('The tokens ', token_list, 'form a subtree of the sentence.')
else: print('The tokens ', token_list, 'do not form a subtree of the sentence.')
print('\n')



## Exercise 4
result4 = get_head_span(doc)
print('The head of the span is: ', result4)
print('\n')



## Exercise 5
result5 = subj_obj_span(doc)  
for key, value in result5.items():
    print('{}\t{}'.format(key, value))

