from DataPreprocessing import preprocess_text, create_vocab, save_vocabulary
from MultinomialNB import MultinomialNB, create_vocab, vectorize_docs
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import pandas as pd 

def main():
    
    '''Marks the start of task 3'''
    # load a preprocess the data
    imdb_data=pd.read_csv('./IMDB-Dataset.csv')
    
    # create a new column which will contain the values of the review that has been processed --> pass in the preprocess_text function directly into this dataframe column
    imdb_data['processed_review']=imdb_data['review'].apply(preprocess_text)
    
    # seperate the first 25k reviews and the rest for testing
    train_data=imdb_data.iloc[:25000]
    test_data=imdb_data.iloc[25000:]
    
    # create vocabulary for the training set --> create_vocab takes in 1 parameter value
    vocabulary=create_vocab(train_data['processed_review'])
    save_vocabulary(vocabulary=vocabulary, file_path='./imdb_vocab.txt')
    
    # vectorize the training and test data
    X_train=vectorize_docs(train_data["processed_review"], vocabulary)
    X_test=vectorize_docs(test_data["processed_review"], vocabulary)
    
    # convert the labels to numeric --> set positive to 1 and negative to 0 --> binary classification
    y_train=np.where(train_data['sentiment']=='positive', 1, 0)
    y_test=np.where(test_data['sentiment']=='positive', 1, 0)
    
    model=MultinomialNB()
    model.fit(X=X_train, y=y_train)
    
    # predict based on the test set data
    predicted_classes=model.predict(X_test)
    predicted_proba=model.predict_log_proba(X_test)
    
    # Model evaluation for the dataset
    accuracy=accuracy_score(y_true=y_test, y_pred=predicted_classes)
    precision=precision_score(y_true=y_test, y_pred=predicted_classes)
    recall=recall_score(y_true=y_test, y_pred=predicted_classes)
    f1=f1_score(y_true=y_test, y_pred=predicted_classes)
    
    # print out the statisitics of the model to see it's performacne
    print(f"Accuracy : {accuracy}")
    print(f"Precision : {precision}")
    print(f"recall : {recall}")
    print(f"f1 score : {f1}")
    
    '''Marks the end fo task 3, below is the implementaiton of task 2'''
    
    documents, labels = zip(*[("fun couple love love comedy", "comedy"),
                              ("fast furious shoot action", "action"),
                              ("couple fly fast fun fun comedy", "comedy"),
                              ("furious shoot shoot fun action", "action"),
                              ("fly fast shoot love action", "action")])
    vocab = create_vocab(documents=documents)
    X_train2=vectorize_docs(docs=documents, vocab=vocab)
    y_train2=np.array([0 if label=='comedy' else 1 for label in labels])
    
    model2=MultinomialNB()
    model2.fit(X=X_train2, y=y_train2)
    
    new_doc="fast couple shoot fly"
    X_test2=vectorize_docs([new_doc], vocab=vocab)
    predicted_class=model2.predict(X=X_test2)
    predicted_proba=model2.predict_log_proba(X=X_test2)
    
    print("Predicted class:", "comedy" if predicted_class[0] == 0 else "action")
    print("Log probabilities:", predicted_proba)
    
    '''Marks the end of task 2'''
    
if __name__=='__main__':
    main()
    
    
    
    