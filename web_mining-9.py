import csv
from nltk import tokenize
import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

inverted_idx = {}

# remove stop words
def remove_stop_words(words):
    filtered = []
    #word = words.split() 
    for r in words: 
        if not r in stop_words:
            filtered.append(r)
    return filtered
    


def get_text_ready(text):
    #tockenize
    tokens = nltk.word_tokenize(text)
    #remove stop words 
    tokens = remove_stop_words(tokens)
    #normalize
    tokens = [word.lower() for word in tokens]
    return tokens
    
    
    
    
text_corpus = []
with open('/Users/rohitbhardwaj/Desktop/JEOPARDY_CSV.csv') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for i, row in enumerate(reader):
        text_corpus
        text = " ".join([row[3], row[5], row[6]])
        filt = get_text_ready(text)   
        for word in filt:
            if word not in inverted_idx:
                inverted_idx[word] = []
            inverted_idx[word].append(i)


def retrive(doc):
    text = []
    with open('/Users/rohitbhardwaj/Desktop/JEOPARDY_CSV.csv') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for i, row in enumerate(reader):
            if i == doc:
                text.append(row[5])
    return text


def search(query):
    result = []
    for word in get_text_ready(query):
        if word in inverted_idx:
            doc_number = inverted_idx[word]
            #result.append(doc_number)
            for i in doc_number:
                ret = retrive(i)
                result.append(ret)
    return result        
    
    
query = input("Enter the search term: ")
search(query)
