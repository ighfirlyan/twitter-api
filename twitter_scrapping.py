import pandas as pd
import re, string
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

df = pd.read_csv('buruh_tweets_202112.csv')
clean_tweet = df['tweet']


def case_folding(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("","", string.punctuation))
    text = text.rstrip().lstrip()
    text = text.replace('   ',' ')

    return text

def tokenizing(text:str):
    '''
    input : string
    output : list of tokens

    memisahkan kalimat menjadi token token kata dan dimasukkan ke dalam sebuah list
    '''
    text_tokens = word_tokenize(text)
    return(text_tokens)

def remove_stopwords(text:str):
    stopwords_engine = StopWordRemoverFactory()
    stopwords = stopwords_engine.get_stop_words()
    
    result = []
    for word in text:
        if word not in stopwords:
            result.append(word)
    return result 

def stemming(text:string):
    '''
    input: string
    output: string

    mengubah bentuk dasar pada kalimat
    '''
    
    engine = StemmerFactory()
    stemmer = engine.create_stemmer()
    text = stemmer.stem(text)

    return text

output=[]

for text in clean_tweet:
    text = case_folding(text)
    text = tokenizing(text)
    text = remove_stopwords(text)
    text = stemming(' '.join(text))
    output.append(text)

output
# new_clean_tweet = pd.DataFrame(output)
# new_clean_tweet.head()