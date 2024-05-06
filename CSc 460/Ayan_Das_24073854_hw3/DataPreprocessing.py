import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re

# Load the IMDB dataset
relative_file_path = './IMDB-Dataset.csv'
# convert it into a dataframe using pandas
imdb_data=pd.read_csv(relative_file_path)

def preprocess_text(text : str) -> str:
    '''
    Clean text by removing HTML tags, puncutations, converting to lowercase, and removing stopwords.
    
    Args : 
        text (Str) : the original text
        
    Returns  :
        str : the Cleaned text.
    '''
    # remove HTML tags
    text=re.sub(r'<.*?>', '', text)
    
    # replace punctuation with Space (words keep intact)
    text=re.sub(r'[^\w\s]', ' ', text)
    
    # convert to lowercase
    text=text.lower()
    
    # remove stopwords
    words=[word for word in text.split() if word not in ENGLISH_STOP_WORDS]
    return ' '.join(words)


# apply preprocessing to each review
imdb_data['processed_review']=imdb_data['review'].apply(preprocess_text)

def create_vocab(reviews: pd.Series) -> list:
    '''
    Create a sorted vocabulary list from a pandas series of text reviews
    
    Args : 
        reviews (pd.series) : Series containing document strings.
        
    Returns : 
        list : Sorted list of unique words
    '''
    # create a vocabulary set
    vocab_set = set()
    
    # Update vocabulary set with words from each review
    reviews.str.split().apply(vocab_set.update)  
    return sorted(vocab_set)


def save_vocabulary(vocabulary : list, file_path : str) -> None:
    '''
    Save the vocabulary list to a text file.
    
    Args:
        vocabular (list) : The vocabulary to save.
        file_path (str) : path to the file where the vocabulary will be saved.
        
    Returns:
        None -> void function
    '''
    # save the vocabulary in a text file
    vocab_file_path='./imdb_vocab.txt'
    with open(vocab_file_path, 'w') as f:
        for word in vocabulary:
            f.write(word+'\n')
        
# display the length of the vocabular and the file path where it's stored
if __name__=='__main__':
    '''
    Purpose : 
        This scripts will run if ran directly, and will be ignored if being outputted to another file
    '''
    print("This script should not run standalone, Please run it from main.py.")
