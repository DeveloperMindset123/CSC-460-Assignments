import numpy as np

class MultinomialNB:
    '''
    - Multinomial Naive Bayes classifier that uses add-one smoothing and log probabillities for classificaiton of discrete number of features
    '''
    
    def __init__(self):
        '''Initialize the class attributes that will be used in the classifier'''
        
        # Log prior probabillities of classes
        self.class_log_prior_ = None
        
        # Log probabillities of features given classes
        self.log_prob_ = None
        
        # Unique classes in the target data
        self.classes_ = None
        
        # Vocabulary lists used for vectorization
        self.vocab_ = None
        
    def fit(self, X : np.ndarray, y : np.ndarray) -> None:
        '''
        - Fit in the Naive Bayes model using the training data
        
        Args:
            X (np.ndarray) : Array of feature vectors (bag-of-words count)
            y (np.ndarray) : Array of target class labels
            
        Returns : None --> void function
        '''
        
        count_sample = X.shape[0]
        self.classes_ = np.unique(y)
        n_classes = len(self.classes_)
        
        # initialzie neccessary matrices
        self.class_log_prior_ = np.zeros(n_classes)
        count = np.zeros((n_classes, X.shape[1]))
        total_count = np.zeros(n_classes)
        
        for c in self.classes_:
            X_c = X[y == c]
            # add one smoothing
            count[c, :] = X_c.sum(axis=0)+1  
            total_count[c]=count[c, :].sum()
            self.class_log_prior_[c]=np.log(X_c.shape[0] / count_sample)
            
        self.log_prob_ = count / total_count[:, np.newaxis]
        
    def predict_log_proba(self, X : np.ndarray) -> np.ndarray:
        '''
        - Predict the log probabillities of the classes for the input samples.
        
        Args : 
            X (np.ndarray) : array of feature vectors to predict
        
        Returns :
            np.ndarray : Array of log probabillities for each class for each input sample.
        '''
        return (X @ (np.log(self.log_prob_).T) + self.class_log_prior_)
    
    def predict(self, X : np.ndarray) -> np.ndarray:
        '''
        - Predict the class labels for input samples.
        
        Args : 
            X (np.ndarray) : Array of feature vectors to predict
            
        Returns : 
            np.ndarray --> Array of predicted class labels
        '''
        return self.classes_[np.argmax(self.predict_log_proba(X), axis=1)]
    
def create_vocab(documents : list) -> list:
    '''
    - Create a vocabulary from a list of documents.
    
    Args : 
        documents (list) : list of document strings
        
    Returns : 
        list : Sorted list of unique words in the documents.
    '''
    vocab = set()
    for doc in documents:
        # add the values from the passed in documents, in this case the document being the csv file that needs to be loaded since that's the dataset we are working with
        vocab.update(doc.split())
        
    # sort the vocab set
    return sorted(vocab)

def vectorize_docs(docs, vocab):
    '''
    - Convert documents to vector form based on the vocabulary.
    
    Args : 
        docs (list) : List of document strings
        vocab (list) : List of unique words
        
    Returns : 
        np.ndarray --> Document-term matrix
    '''
    vocab_index = {word : i for i, word in enumerate(vocab)}
    vectors = np.zeros((len(docs), len(vocab)), dtype=int)
    for i, doc in enumerate(docs):
        for word in doc.split():
            if word in vocab_index:
                vectors[i, vocab_index[word]] += 1
    return vectors

'''Function body that is to be run within main.py'''
if __name__ == '__main__':
    '''
    Purpose : 
        This scripts will run if ran directly, and will be ignored if being outputted to another file
    '''
    # small corpus with labels
    corpus = [
        ("fun couple love love comedy", "comedy"),
        ("fast furious shoot action", "action"),
        ("couple fly fast fun fun comedy", "comedy"),
        ("furious shoot shoot fun action", "action"),
        ("fly fast shoot love action", "action")
    ]


    # new document
    new_doc = "fast couple shoot fly"

    # prepare training data
    documents, labels = zip(*corpus)

    # create vocab from the documents and vectorize the documents
    vocab = create_vocab(documents=documents)
    X_train=vectorize_docs(documents, vocab=vocab)
    # encoding --> labels : comedy -> 0, action -> 1
    y_train=np.array([0 if label=='comedy' else 1 for label in labels])

    # fit model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # predict the new document
    X_test = vectorize_docs([new_doc], vocab)
    predicted_class = model.predict(X_test)
    predicted_proba=model.predict_log_proba(X_test)

    # it's either comedy or action
    print("Predicted class:", "comedy" if predicted_class[0] == 0 else "action")
    print("Log probabilities:", predicted_proba)

            
            
        